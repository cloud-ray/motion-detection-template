# utils/performance_utils.py
import time

def calculate_fps(frame_times, start_time, fps_display_interval):
    """
    Calculates the frames per second (FPS) based on the recorded frame times and elapsed time.
    
    Parameters:
    - frame_times (list of float): List of timestamps when each frame was processed.
    - start_time (float): The start time for measuring FPS.
    - fps_display_interval (float): The interval in seconds for displaying FPS.
    
    Returns:
    - float: The calculated FPS.
    - list of float: The updated list of frame times.
    - float: The updated start time for the next FPS calculation.
    """
    current_time = time.time()
    frame_times.append(current_time)
    
    # Calculate elapsed time
    elapsed_time = current_time - start_time if start_time else 0
    
    if elapsed_time > fps_display_interval:
        # Calculate average FPS based on the number of frames and elapsed time
        fps = len(frame_times) / elapsed_time
        frame_times.clear()  # Clear the list
        start_time = current_time  # Reset the start time
    else:
        fps = len(frame_times) / elapsed_time if elapsed_time > 0 else 0
    
    return fps, frame_times, start_time
