#!/usr/bin/python3

#importing opencv lib
import cv2

#capting voideo in an object. 0 attribute defines the default camera source
cap = cv2.VideoCapture(0)

#Video is a continous sequence of franes. Creating infinite loop to show to frames continously. 
while True:

    #Readtingg the video source object and storing each frame in the "frame"
    #"success" returns a boolean value for the frame storage operation
    sucess, frame = cap.read()

    #Displaying frame by frame in a window a video
    cv2.imshow("Video", frame)

    #dislplaying the each frame for 1ms and quitting by pressing "q" 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#releasing the source camera 
cap.release()

#to distroy all the windows we created
cv2.destroyAllWindows()
