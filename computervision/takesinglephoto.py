import time
import numpy as np
import cv2 as cv

def get_image():
    cap = cv.VideoCapture(0)
    # Capture frame, frame is image
    ret, frame = cap.read()
    print(ret, frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # convert to gray scale
    # save the frame
    cv.imwrite(r"C:/Users/Laptop/Desktop/a.png", gray)

get_image()
