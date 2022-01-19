#opencv5
import cv2
import numpy as np

resim=cv2.imread("img.jfif")

print(resim[100,100]) # this pixel is [60,76,143] blue is 60 green is 76 red is 143 so this color of picture look like red because number of red is so high other ones.
#I can change the pixel color
resim[20,100]=[0,0,0]
for i in range(190):
    resim[10,i]=[255,255,255]
    resim[110,i]=[255,255,255]
    resim[210,i]=[255,255,255]
    for k in range(266):
        resim[k,50]=[255,255,255]
        resim[k,130]=[255,255,255]
img=resim[10:110,50:130]
resim[10:110,50:130]=img
#resim[10:110,40:120]=img
resim[110:210,50:130]=img

b,g,r=cv2.split(resim)
c=cv2.merge((b,g,r))
cv2.imshow("img Blue",b)
cv2.imshow("img Green",g)
cv2.imshow("img Red",r)
cv2.imshow("img Merge",c)
cv2.imshow("img",img)
resim[10:110,50:130,2]=255#makes the color of the part it receives red 255
resim[10:110,50:130,0]=255
resim[110:210,50:130,1]=255
resim[110:210,50:130,0]=255
#reason to equalize it makes full red to 255

cv2.imshow("img",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
