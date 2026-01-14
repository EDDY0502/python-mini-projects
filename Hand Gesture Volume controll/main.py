import cv2  # Import OpenCV (cv2), the main library used for camera input, image capture, drawing shapes, text, etc.

import time  # Import the time module; we will use it to calculate FPS (frames per second) to monitor performance.

import numpy as np  # Import NumPy, used for fast mathematical operations like interpolation (mapping one range to another).

import HandTrackingModule as htm  # Import our custom module "HandTrackingModule" that detects hands and returns finger positions.

import math  # Import the math module; we will use its hypot() function to measure exact distance between two fingers.

from pycaw.pycaw import AudioUtilities  # Import AudioUtilities from pycaw; this lets us access system audio devices like speakers/headphones.

from ctypes import cast, POINTER  # Import cast and POINTER to convert Windows audio objects into usable Python pointer objects.

from comtypes import CLSCTX_ALL  # Import CLSCTX_ALL for context activation; required when initiating audio control objects.

from pycaw.pycaw import IAudioEndpointVolume  # Import the interface that allows us to set and adjust system volume levels.

# -------------------------------------------------------- #
# WEBCAM SETUP (RESOLUTION SETTING)
# -------------------------------------------------------- #

wCam, hCam = 1280, 720  # Define the desired width (wCam) and height (hCam) for the webcam capture window (HD resolution 1280x720).

cap = cv2.VideoCapture(0)  # Create a VideoCapture object named "cap" and connect it to webcam at index 0 (default laptop camera).

cap.set(3, wCam)  # Set camera property ID 3 to 1280 → adjusts the width of the webcam feed to our chosen resolution.

cap.set(4, hCam)  # Set camera property ID 4 to 720 → adjusts the height of the webcam feed to our chosen resolution.

pTime = 0  # A variable that will store last frame timestamp; we use it to compute FPS every frame.

# -------------------------------------------------------- #
# HAND DETECTION SETUP
# -------------------------------------------------------- #

dectector = htm.handDetector(detectionCon=0.7)  
# Create a handDetector object using our imported module.
# detectionCon=0.7 means the detector must be at least 70% confident to recognize a hand.
# This reduces false hand detections and provides more stable tracking.

# -------------------------------------------------------- #
# SYSTEM AUDIO CONTROL SETUP (PYCAW)
# -------------------------------------------------------- #

device = AudioUtilities.GetSpeakers()  
# Access the default playback device (usually speakers/headphones).
# This object tells us WHICH audio device to control.

volumeCtrl = device.EndpointVolume  
# "EndpointVolume" gives us control over volume of the chosen audio device (Mute, Increase, Decrease, Scalar, etc.).

volRange = volumeCtrl.GetVolumeRange()  
# Get the entire available volume range in decibels (dB). 
# On Windows, this usually returns values like [-65.25, 0.0] where -65 is silent and 0 is 100% max loudness.

minVol = volRange[0]  # Store minimum volume value (silent level in dB).
maxVol = volRange[1]  # Store maximum volume value (loudest possible system volume in dB).


# -------------------------------------------------------- #
# MAIN LOOP (RUNS UNTIL USER PRESSES ESC)
# -------------------------------------------------------- #

while True:  # Start an infinite loop to continuously process webcam frames.

    success, img = cap.read()  
    # Read a frame from the webcam using cap.read().
    # 'success' is True if frame captured correctly.
    # 'img' is the actual image captured from the camera.



    img = dectector.findHands(img)  
    # Pass the captured image to the hand detection method.
    # It draws hand landmarks on the image and returns the modified frame with hands marked.

    lmList, bbox = dectector.findPosition(img, draw=False)  
    # FindPosition returns a list containing 21 different hand landmark positions (x, y coordinate of each joint).
    # lmList = list of finger landmark coordinates.
    # bbox = bounding box around the detected hand.
    # draw=False means we don’t draw circles or box from this function (we will draw manually later).

    # -----------------------------
    # If at least ONE hand is detected
    # -----------------------------

    if len(lmList) != 0:  
        # If lmList is NOT empty → means a hand is detected and landmark data is available.

        x1, y1 = lmList[4][1], lmList[4][2]  
        # Extract coordinates of thumb tip (landmark 4) from lmList.
        # lmList[4] contains [id, x, y], so [1] = x coordinate, [2] = y coordinate.

        x2, y2 = lmList[8][1], lmList[8][2]  
        # Extract coordinates of index finger tip (landmark 8).

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  
        # Calculate midpoint between thumb and index finger tips.
        # We use integer division // for a clean integer pixel value.

        # -------------------------------------------------- #
        # DRAW DETECTION FEEDBACK (FINGER CIRCLES/LINE)
        # -------------------------------------------------- #

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)  
        # Draw a filled purple circle at thumb position → makes the tracking visual for user.

        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)  
        # Draw a filled purple circle at index finger position.

        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)  
        # Draw a white line between thumb & index finger to visualize distance.

        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)  
        # Draw another circle at the midpoint between fingers for design/visual feedback.

        # -------------------------------------------------- #
        # MEASURE DISTANCE BETWEEN FINGERS (GESTURE SIZE)
        # -------------------------------------------------- #

        length = math.hypot(x2 - x1, y2 - y1)  
        # math.hypot(dx, dy) calculates Euclidean distance between two points (pythagoras).
        # This gives the EXACT physical length between thumb and index finger.

        # -------------------------------------------------- #
        # MAP FINGER DISTANCE TO SYSTEM VOLUME (INTERPOLATION)
        # -------------------------------------------------- #

        volValue = np.interp(length, [50, 250], [minVol, maxVol])  
        # Convert hand distance into a meaningful volume value using interpolation.
        # If distance = 50 pixels → set volume to minVol.
        # If distance = 300 pixels → set volume to maxVol.

        volumeCtrl.SetMasterVolumeLevel(volValue, None)  
        # Apply the calculated volume to the system.
        # This changes Windows volume instantly based on finger distance.

        # -------------------------------------------------- #
        # VISUAL FEEDBACK WHEN FINGERS GET CLOSE
        # -------------------------------------------------- #

        if length < 50:  
            # If thumb and index finger distance is VERY small (pinched position):

            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)  
            # Replace midpoint circle with green color to indicate "minimum gesture distance".

        # -------------------------------------------------- #
        # DRAW VOLUME BAR BASED ON HAND MOVEMENT
        # -------------------------------------------------- #

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        # Draw border rectangle for the volume bar scale at left side of screen.

        cv2.rectangle(img, (50, int(np.interp(length, [50, 300], [400, 150]))),
                      (85, 400), (0, 255, 0), cv2.FILLED)
        # The inner rectangle shows active volume level based on finger distance mapping.
        # As the hand spreads, the inner fill rectangle grows upwards.


    # -------------------------------------------------- #
    # ⏱ FPS CALCULATION + DISPLAY
    # -------------------------------------------------- #

    cTime = time.time()  # Get current system timestamp.

    fps = 1 / (cTime - pTime)  # FPS = 1 / time taken to render one frame.

    pTime = cTime  # Update previous time to current time for next frame calculation.

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    # Display FPS on top left to track performance.


    # -------------------------------------------------- #
    # DISPLAY FINAL IMAGE FRAME
    # -------------------------------------------------- #

    cv2.imshow("Img", img)  
    # Show final frame in a window titled "Img".

    # -------------------------------------------------- #
    # EXIT PROGRAM WHEN USER PRESSES ESC KEY
    # -------------------------------------------------- #

    key = cv2.waitKey(1)  # Wait for 1 millisecond; captures keyboard press.

    if key == 27:  # 27 is ASCII code for ESC key.
        break  # Break loop and exit program safely.


# -------------------------------------------------- #
# RELEASE CAMERA AND CLOSE WINDOWS
# -------------------------------------------------- #

cap.release()  # Release camera resource so it can be used by other programs.

cv2.destroyAllWindows()  # Close all OpenCV windows to properly terminate application.
