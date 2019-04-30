# -*-coding: utf-8 -*-
import cv2
import numpy as np
import time
import cv_RC


cap = cv2.VideoCapture(0)



print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))
cap.set(3, 320)
cap.set(4, 240)
cv_RC.STOP()

while (True):

    red_count = 0
    green_count = 0
    ret, frame = cap.read()
    px = frame[160, 120]

    if green_count > 12000:
        cv_RC.GO()
        green_count = 0
    if red_count > 12000:
        cv_RC.STOP()
        red_count = 0
    if (ret):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(px)
        cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break
    if px[0] >= 69 and px[1] >= 68 and px[2] >= 250 and px[0] <= 101 and px[1] <= 78 and px[2] <= 255:  # RED
        cv_RC.STOP()
        print("stop")
    if px[0] >= 43 and px[1] >= 137 and px[2] >= 20 and px[0] <= 171 and px[1] <= 248 and px[2] <= 90:  # GREEN
        cv_RC.GO()
        print("GO")

cap.release()
cv2.destroyAllWindows()