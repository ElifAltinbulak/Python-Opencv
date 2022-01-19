#opencv3
import cv2
import numpy as np
img=cv2.imread("img.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img show
cv2.imshow("img",img)
cv2.imshow("img_gray",img_gray)
#new record
cv2.imwrite("new_img_gray.jpg",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
