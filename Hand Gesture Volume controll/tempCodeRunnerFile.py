import cv2 # type: ignore
import time
import numpy as np # type: ignore
import HandTrackingModule as htm # type: ignore
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL # type: ignore
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume # type: ignore


##################################
wCam,hCam = 1280 , 720
##################################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

dectector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(0, None)




while True:
  success, img = cap.read()
  img=dectector.findHands(img)
  lmList,bbox = dectector.findPosition(img,draw=False)
  if len(lmList)!=0:
    #print(lmList[4],lmList[8])

    x1, y1 = lmList[4][1], lmList[4][2]   # Thumb tip
    x2, y2 = lmList[8][1], lmList[8][2]   # Index finger tip
    cx,cy = (x1 + x2)//2 , (y1 + y2)//2

    cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
    cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    length = math.hypot(x2 - x1, y2 - y1)
    print(length)

    if length < 50:
      cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)


  cTime = time.time()
  fps = 1 / (cTime - pTime)
  pTime = cTime

  cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

  cv2.imshow("Img",img)
  cv2.waitKey(1)


