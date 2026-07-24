import cvzone # type: ignore
import cv2 # type: ignore
import numpy as np # type: ignore
from cvzone.HandTrackingModule import HandDetector # type: ignore

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector= HandDetector(detectionCon=0.8, maxHands=2)

while True:
  success, img = cap.read()
  img=cv2.flip(img,1)
  hand,img=detector.findHands(img, flipType=False)
  cv2.imshow("Image", img)
  cv2.waitKey(1)

  


