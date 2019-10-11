import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite("img.jpg", frame)
    break

# When everything done, release the capture
cap.release()