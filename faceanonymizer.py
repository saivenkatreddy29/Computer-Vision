import os
import argparse

import cv2
import mediapipe as mp


image_path = r"C:\Users\saive\Desktop\Github\Computer-Vision\images\face.png"
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
face_detection = mp.solutions.face_detection
out = face_detection.process(image_rgb)
print(out)