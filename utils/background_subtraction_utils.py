# background_subtraction_utils.py
import cv2
from configs.config import BACKGROUND_SUBTRACTOR_HISTORY, BACKGROUND_SUBTRACTOR_VAR_THRESHOLD, BACKGROUND_SUBTRACTOR_DETECT_SHADOWS, SCALE_X, SCALE_Y

def initialize_background_subtractor(
        history=BACKGROUND_SUBTRACTOR_HISTORY, 
        varThreshold=BACKGROUND_SUBTRACTOR_VAR_THRESHOLD, 
        detectShadows=BACKGROUND_SUBTRACTOR_DETECT_SHADOWS
    ):
    """
    Initializes and returns a background subtractor using the MOG2 algorithm with configurable parameters.
    
    Parameters:
    - history (int): The number of previous frames used to model the background. Default is from config.
    - varThreshold (float): The threshold on the squared Mahalanobis distance between the pixel and the model, used to classify a pixel as foreground. Default is from config.
    - detectShadows (bool): Whether to detect shadows in addition to foreground objects. Default is from config.
    
    Returns:
    - cv2.BackgroundSubtractorMOG2: The initialized background subtractor object.
    
    The background subtractor is used to separate moving objects (foreground) from the static background in a video stream.
    """
    return cv2.createBackgroundSubtractorMOG2(history=history, varThreshold=varThreshold, detectShadows=detectShadows)

def process_frame(frame, backSub):
    """
    Processes a single video frame by resizing, converting to grayscale, applying Gaussian blur, and performing background subtraction.
    
    Parameters:
    - frame (numpy.ndarray): The original video frame to be processed.
    - backSub (cv2.BackgroundSubtractorMOG2): The background subtractor object used to generate the foreground mask.
    
    Returns:
    - resized_frame (numpy.ndarray): The resized frame, scaled according to SCALE_X and SCALE_Y.
    - fg_mask (numpy.ndarray): The foreground mask obtained by applying the background subtractor to the blurred grayscale frame.
    - thresh (numpy.ndarray): The binary thresholded image of the foreground mask, used for motion detection.
    
    The frame is first resized, then converted to grayscale, blurred to reduce noise, and finally processed to obtain the foreground mask and binary threshold image.
    """
    resized_frame = cv2.resize(frame, (0, 0), fx=SCALE_X, fy=SCALE_Y)
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    fg_mask = backSub.apply(blurred_frame)
    _, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
    return resized_frame, fg_mask, thresh
