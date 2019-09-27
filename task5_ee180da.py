import numpy as numpy
import cv2

cap = cv2.VideoCapture(0)
rows = 75;
columns = 75;
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (int(cap.get(3)), int(cap.get(4))), 0)

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

#ret, frame = cap.read()
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#cv2.imshow('frame', gray)
#cv2.imwrite('./test2.png', gray)
#img = cv2.imread('./test2.png', cv2.IMREAD_UNCHANGED)
#resized = cv2.resize(img, (rows, columns), interpolation = cv2.INTER_AREA)
#cv2.imwrite('./test.png', resized)

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

#scale = "@%#*+=-:. " # 10 levels of grayscale
#file = "file_name.txt"

#grayscale = cv2.imread("test.png", 0)
#for x in grayscale:
#	for y in x:
#		f = open(file, 'a')
#		f.write( scale[y//26] )
#		f.close()
#	f = open(file, 'a')
#	f.write( "\n" )
#	f.close()
#


