import cv2
import numpy as np
from utils import get_limits
from PIL import Image

blue = [255,0,0]
cap = cv2.VideoCapture(0)

while True:
    res,frame = cap.read()
    
    # print(frame)
    # print('\n')
    hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # print(hsv_image)
    lowerlimit,upperlimit = get_limits(blue)
    mask = cv2.inRange(hsv_image,lowerlimit,upperlimit)
    print(f'mask is {mask}')
    mask_ = Image.fromarray(mask)
    print(f'mask image is {mask_}')
    bbox = mask_.getbbox()
    print(f'box is {bbox}')
    # if bbox is not None:
    #     x1,y1,x2,y2 = bbox
    #     frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    # cv2.imshow('frame',frame)
    # # cv2.imshow('hsv frame',hsv_image)
    # if cv2.waitKey(40) & 0xFF == ord('q'):
    #     break
    # break

cap.release()
cv2.destroyAllWindows()
