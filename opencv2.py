#opencv2
import cv2
img=cv2.imread("img.jpg",0)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#or
cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)
cv2.destroyAllWindows()
