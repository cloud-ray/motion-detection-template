# config.py

# Video Stream URL
VIDEO_STREAM_URL = "http://192.168.4.24:8080/video"

# Background Subtractor Parameters
BACKGROUND_SUBTRACTOR_HISTORY = 300
BACKGROUND_SUBTRACTOR_VAR_THRESHOLD = 100
BACKGROUND_SUBTRACTOR_DETECT_SHADOWS = True

# Frame Processing Parameters
PROCESS_INTERVAL = 3  # Process every nth frame
FPS_DISPLAY_INTERVAL = 1  # Display FPS every n seconds
PRINT_INTERVAL = 25  # Print information every n frames

# Motion Detection Parameters
MOTION_THRESHOLD = 1000  # Pixels threshold to detect motion

# Scaling Parameters
SCALE_X = 0.5  # Scale factor for width
SCALE_Y = 0.5  # Scale factor for height

# Object Detection Parameters (if applicable)
COOLDOWN_PERIOD = 5  # Cooldown period in seconds
