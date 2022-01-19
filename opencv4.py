#opencv4
#firstly,the pictures are arranged with RGB logic, but opencv should also be BGR
import cv2
import numpy as np
img=cv2.imread("img.jpg")
print(img)
"""
   B   G   R
[[[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]
  ...
  ]



"""
cv2.waitKey(0)
cv2.destroyAllWindows()
