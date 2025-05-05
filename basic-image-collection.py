import cv2
import uuid
import os
import random
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened(): 
    ret, frame = cap.read()
   
    # Cut down frame to 250x250px
    frame = frame[120:120+250,200:200+250, :]
    
    # Collect anchors 
    if cv2.waitKey(1) & 0XFF == ord('a'):
        # Create the unique file path 
        imgname = os.path.join(f"anchors/{uuid.uuid1()}.jpg")

        # Write out anchor image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(imgname, frame)
    
        print("a")
    
    # Collect positives
    if cv2.waitKey(1) & 0XFF == ord('p'):
        # Create the unique file path 
        imgname = os.path.join(f"positives/{uuid.uuid1()}.jpg")

        # Write out positive image
        cv2.imwrite(imgname, frame)

        print("p")
    
    # Show image back to screen
    cv2.imshow('Image Collection', frame)
    
    # Breaking gracefully
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
        
# Release the webcam
cap.release()

# Close the image show frame
cv2.destroyAllWindows()