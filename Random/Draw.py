import cvzone  # type: ignore
import cv2  # type: ignore
import numpy as np  # type: ignore
from cvzone.HandTrackingModule import HandDetector  # type: ignore
import math

# ---------------- CAMERA SETUP ---------------- #
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
print("Camera opened:", cap.isOpened())  # check camera

detector = HandDetector(detectionCon=0.8, maxHands=1)


# ---------------- SNAKE CLASS ---------------- #
class SnakeGameClass:
    def __init__(self):
        self.points = []          # snake points
        self.lengths = []         # lengths between points
        self.currentLength = 0    # total length of snake
        self.allowedLength = 150  # max length
        self.previousHead = (0, 0)

    def update(self, imgMain, currentHead):
        px, py = self.previousHead
        cx, cy = currentHead

        # First frame fix
        if px == 0 and py == 0:
            self.previousHead = cx, cy
            return imgMain

        # Add snake segments
        self.points.append([cx, cy])
        distance = math.hypot(cx - px, cy - py)
        self.lengths.append(distance)
        self.currentLength += distance
        self.previousHead = (cx, cy)

        # Draw lines for snake body
        for i in range(1, len(self.points)):
            cv2.line(imgMain, tuple(self.points[i - 1]), tuple(self.points[i]), (0, 0, 255), 20)

        # Draw head
        cv2.circle(imgMain, tuple(self.points[-1]), 20, (200, 0, 200), cv2.FILLED)

        return imgMain


# ---------------- MAIN PROGRAM LOOP ---------------- #
game = SnakeGameClass()

while True:
    success, img = cap.read()
    if not success:
        print("Camera Error!")
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        fingers = detector.fingersUp(hands[0])  # returns [thumb, index, middle, ring, pinky]

        # 🖐 If 5 fingers up → Erase screen
        if fingers == [1, 1, 1, 1, 1]:
            game = SnakeGameClass()
            cv2.putText(img, "Erase", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

        # ✌ If only INDEX + MIDDLE → Pause
        elif fingers == [0, 1, 1, 0, 0]:
            cv2.putText(img, "Pause", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)

        # ☝ If only INDEX → Draw
        elif fingers == [0, 1, 0, 0, 0]:
            lmList = hands[0]["lmList"]
            pointIndex = lmList[8][0:2]  # index finger coordinates
            img = game.update(img, pointIndex)

    cv2.imshow("Image", img)

    # Exit if window closed manually
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
        break

    # ESC key to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
