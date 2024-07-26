# main.py
import time
import cv2
from utils.background_subtraction_utils import initialize_background_subtractor, process_frame
from utils.display_utils import display_video_frames, display_performance_info
from utils.motion_detection_utils import detect_motion
from utils.performance_utils import calculate_fps
from utils.video_utils import initialize_video_capture, get_video_properties
from configs.config import *

def main():
    """
    Main function to capture video, process frames, and detect motion.

    Initializes video capture, background subtraction, and various settings for processing and displaying video.
    Monitors frames to detect motion and provides real-time feedback on motion detection status.

    The function performs the following steps:
    1. Initializes video capture and background subtraction.
    2. Processes video frames to detect motion.
    3. Displays video frames and performance metrics.
    4. Provides feedback on motion detection status.
    5. Exits on user input ('q' key).

    Settings:
        - VIDEO_STREAM_URL: URL of the video stream.
        - BACKGROUND_SUBTRACTOR_HISTORY: History parameter for background subtractor.
        - BACKGROUND_SUBTRACTOR_VAR_THRESHOLD: Variance threshold for background subtractor.
        - BACKGROUND_SUBTRACTOR_DETECT_SHADOWS: Flag to detect shadows.
        - PROCESS_INTERVAL: Interval in frames for processing.
        - FPS_DISPLAY_INTERVAL: Interval in seconds for displaying FPS.
        - MOTION_THRESHOLD: Threshold for detecting motion in pixels.
        - PRINT_INTERVAL: Interval in frames for printing performance info.

    Exits:
        - Press 'q' key to exit the loop and close the video stream.
    """
    cap = initialize_video_capture(VIDEO_STREAM_URL)
    fps = get_video_properties(cap)
    backSub = initialize_background_subtractor(
        history=BACKGROUND_SUBTRACTOR_HISTORY,
        varThreshold=BACKGROUND_SUBTRACTOR_VAR_THRESHOLD,
        detectShadows=BACKGROUND_SUBTRACTOR_DETECT_SHADOWS
    )
    
    frame_counter = 0
    frame_times = []
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame")
            break
        
        frame_counter += 1
        if frame_counter % PROCESS_INTERVAL != 0:
            continue

        frame_start_time = time.time()
        resized_frame, fg_mask, thresh = process_frame(frame, backSub)
        motion_detected = detect_motion(thresh, motion_threshold=MOTION_THRESHOLD)

        if motion_detected:
            print("Motion Detected")
        else:
            print("Motion Not Detected")

        motion_detection_latency = time.time() - frame_start_time
        fps, frame_times, start_time = calculate_fps(frame_times, start_time, FPS_DISPLAY_INTERVAL)
        display_video_frames(resized_frame, fg_mask)
        if frame_counter % PRINT_INTERVAL == 0:
            display_performance_info(motion_detection_latency, fps, frame_counter, PRINT_INTERVAL)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
