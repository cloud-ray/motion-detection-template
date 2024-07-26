# utils/motion_detection_utils.py
import cv2
from configs.config import MOTION_THRESHOLD

def detect_motion(thresh, motion_threshold=MOTION_THRESHOLD):
    """
    Detects motion in a given thresholded image based on a specified motion threshold.
    
    Parameters:
    - thresh (numpy.ndarray): The binary image obtained after applying a threshold to the foreground mask.
    - motion_threshold (int): The minimum number of non-zero pixels required to consider motion detected. Default is 1000.
    
    Returns:
    - bool: True if the number of non-zero pixels exceeds the motion_threshold, otherwise False.
    """
    motion_pixels = cv2.countNonZero(thresh)
    return motion_pixels > motion_threshold
