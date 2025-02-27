import os
import argparse

import cv2
import mediapipe as mp


def process_image(img,face_detection):

    H,W,_ = img.shape
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    

args = argparse.ArgumentParser()
args.add_argument('--mode',default = 'image')
args.add_argument('--filepath',default = r"C:\Users\saive\Desktop\Github\Computer-Vision\images\face.png")
args = args.parse_args()

mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection = 0, min_detection_confidence = 0.5) as face_detection:
    if args.mode in ['image']:

        # read image
        img = cv2.imread(args.filepath)
        img = process_image(img,face_detection)
