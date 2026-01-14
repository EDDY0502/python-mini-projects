import cv2
import mediapipe as mp #to detact hand
import pyautogui #to move the mouse 

cap =cv2.VideoCapture(0) #capture video
hand_dectector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils #to get lines on hand
screen_weidth,screen_height= pyautogui.size() #to get the size of your screen
index_y=0

cv2.namedWindow('Virtual Mouse', cv2.WINDOW_NORMAL)  # make window resizable
cv2.setWindowProperty('Virtual Mouse', cv2.WND_PROP_TOPMOST, 1)  # keep on top

while True:
    _,frame=cap.read() #1st variable is empty 2nd is frame
    frame=cv2.flip(frame,1) #to unmirror the flame , 0=flip xaxis 1=flip yaxis
    frame_height,frame_width,_=frame.shape  #It means: “I don’t care about this value.”
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #convert colour
    output=hand_dectector.process(rgb_frame) #to process the detactor
    hands= output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand) #to get line on the hand 
            landmarks = hand.landmark #landmark are points on hand
            for id,landmarks in enumerate(landmarks): #enumerate are numbers on hand
                x=int(landmarks.x*frame_width)
                y=int(landmarks.y*frame_height)

                if id==8: #index finger 
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255), thickness=-1)
                    index_x=screen_weidth/frame_width*x
                    index_y=screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                
                if id==4: #thumb finger
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255), thickness=-1)
                    thumb_x=screen_weidth/frame_width*x
                    thumb_y=screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))

                    if abs(index_y - thumb_y)<20:
                        pyautogui.click()
                        print("click")  # print when clicked

    cv2.imshow('Virtual Mouse',frame) #what i wanna show
    cv2.waitKey(1)  #to display
