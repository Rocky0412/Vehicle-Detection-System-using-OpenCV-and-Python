import cv2
import numpy as np
while True:
    ret,frame1=cap.read()
    cv2.imshow('Video original',frame1)
    if cv2.waitKey(1)==13:
        break
        
cv2.destroyAllWindows()
cap.release()