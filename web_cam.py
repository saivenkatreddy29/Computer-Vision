# Read using the webcam
import cv2
import numpy
import torch


web_key = True

web_video = cv2.VideoCapture(0)
while web_key:
    web_key,frame = web_video.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

web_video.release()
cv2.destroyAllWindows()
