#opencv6
img=cv2.imread("img.jpg")
print(img[50:50])
#this situation is 50 on the x-axis, 50 on the y-axis, exactly the BGR values ​​of that pixel
for i in range(200):
    img[50:i]=img[255,255,255]
    #we changed that whole row or column and made it white.
part=img[100:300,200:400]#[y1:y2,x1:x2]
cv2.imshow("new_img",part)
