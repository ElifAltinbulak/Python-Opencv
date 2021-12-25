import cv2
import numpy as np
resim=np.zeros((600,600,3),"uint8")
resim.fill(255)
cv2.putText(resim,"Homework",(130,230),cv2.FONT_HERSHEY_COMPLEX,2,(250,254,1))
cv2.circle(resim,(300,300),50,(255,0,0),2)
cv2.rectangle(resim,(250,350),(350,250),(0,255,0),2)
cv2.line(resim,(250,350),(350,250),(255,255,0),2)
cv2.line(resim,(250,250),(350,350),(0,255,255),2)
cv2.imshow("Homework",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
