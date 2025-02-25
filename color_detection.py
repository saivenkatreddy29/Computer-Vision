import cv2
import numpy as np
from utils import get_limits

yellow = [0,255,255]
cap = cv2.VideoCapture(0)

while True:
    res,frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
