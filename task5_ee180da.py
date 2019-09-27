import numpy as numpy
import cv2


## first we record the video frame by frame
cap = cv2.VideoCapture(0)
rows = 75;
columns = 75;
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (int(cap.get(3)), int(cap.get(4)))   )

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
    	out.write(frame)
    	cv2.imshow('frame', frame)

    	if cv2.waitKey(5) & 0xFF == ord('q'):
        	break

    else:
    	break

cap.release()
out.release()
cv2.destroyAllWindows()




cap = cv2.VideoCapture('outpy.avi')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break



