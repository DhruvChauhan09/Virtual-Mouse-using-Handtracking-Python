import cv2
import mediapipe as mp
import time
import pyautogui 
import numpy as np
import mymodule as mm

cap = cv2.VideoCapture(0)
detector=mm.handDetector()
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height


screen_width, screen_height = pyautogui.size()
prev_x, prev_y = 0, 0
smoothening = 7  #~

frame_width, frame_height = 640, 480

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmList = detector.findPosition(img)

    if lmList:
        x1,y1 = lmList[8][1:]   #index_tip
        x2,y2 = lmList[4][1:]   #thumb_tip

        cv2.circle(img, (x1, y1), 8, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 8, (255, 0, 0), cv2.FILLED)  

        # Convert coordinates
        screen_x = np.interp(x1, (0, frame_width), (0, screen_width))
        screen_y = np.interp(y1, (0, frame_height), (0, screen_height))

        # Smooth movement
        curr_x = prev_x + (screen_x - prev_x) / smoothening
        curr_y = prev_y + (screen_y - prev_y) / smoothening

        pyautogui.moveTo(screen_width - curr_x, curr_y)
        prev_x, prev_y = curr_x, curr_y  

        distance = np.hypot(x2-x1,y2-y1)

        if distance<25:
            cv2.circle(img, ((x1 + x2) // 2, (y1 + y2) // 2), 10, (0, 255, 0), cv2.FILLED)
            pyautogui.doubleClick()
            time.sleep(0.2)

    

    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break