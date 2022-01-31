import cv2
import numpy as np
babür=cv2.imread("baburaile.jpg")
images=cv2.imread("images.png")
print(f"Babür shape:{babür.shape}\nİmages:{images.shape}")
h,g,c=images.shape
new=babür[0:h,0:g]
inverst=cv2.bitwise_not(images)
add=cv2.add(new,inverst)
babür[0:h,0:g]=add
#cv2.imshow("add",add)
#cv2.imshow("inverst",inverst)
#cv2.imshow("new",new)
cv2.imshow("heyo",babür)
#cv2.imshow("images",images)
cv2.waitKey(0)
cv2.destroyAllWindows()
