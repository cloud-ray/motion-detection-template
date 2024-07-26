# utils/video_utils.py
import cv2

def initialize_video_capture(url):
    """
    Initializes video capture from the given URL.
    
    Parameters:
    - url (str): The URL of the video stream.
    
    Returns:
    - cv2.VideoCapture: The VideoCapture object for the video stream.
    
    Raises:
    - ValueError: If the video stream cannot be opened.
    """
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        raise ValueError("Error: Unable to open video stream")
    return cap

def get_video_properties(cap):
    """
    Retrieves and prints the properties of the video stream.
    
    Parameters:
    - cap (cv2.VideoCapture): The VideoCapture object for the video stream.
    
    Returns:
    - float: The frames per second (FPS) of the video stream.
    """
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"Original FPS: {fps}")
    print(f"Frame Width: {frame_width}")
    print(f"Frame Height: {frame_height}")
    return fps
