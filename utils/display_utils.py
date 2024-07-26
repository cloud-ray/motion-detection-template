# utils/display_utils.py
import cv2
import psutil

def display_video_frames(resized_frame, fg_mask):
    """
    Displays the video frames and foreground mask in separate windows.
    
    Parameters:
    - resized_frame (numpy.ndarray): The frame from the video stream, resized according to the scaling factors.
    - fg_mask (numpy.ndarray): The foreground mask obtained from background subtraction.
    
    The function uses OpenCV's imshow to display the frames.
    """
    cv2.imshow('Video Stream', resized_frame)
    cv2.imshow('Foreground Mask', fg_mask)

def display_performance_info(motion_detection_latency, fps, frame_counter, print_interval):
    """
    Prints performance information if the frame counter is a multiple of the print_interval.
    
    Parameters:
    - motion_detection_latency (float): The latency of the motion detection process in seconds.
    - fps (float): The frames per second (FPS) of the video stream.
    - frame_counter (int): The count of frames processed so far.
    - print_interval (int): The interval at which to print the performance information (in frames).
    
    The function displays the latency, FPS, CPU usage, and memory usage.
    """
    if frame_counter % print_interval == 0:
        print(f"Motion Detection Latency: {motion_detection_latency:.6f} seconds, FPS: {fps:.2f}, "
              f"CPU Usage: {psutil.cpu_percent():.2f}%, Memory Usage: {psutil.virtual_memory().percent:.2f}%")
