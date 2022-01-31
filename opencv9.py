import cv2
import numpy as np
kamera=cv2.VideoCapture(0)
dusuk=np.array([0,100,100])
yuksek=np.array([22,255,255])
#bunun sebebi ise hsv aralığını almaktı 
while True:
    ret,kare=kamera.read()
    hsv=cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
    #burdan itibaren hsv formundan mask yapmamamız gerekir 
    #bunun sebebi ise istenilen renge daha rahat ulaşmak için
    mask=cv2.inRange(hsv,dusuk,yuksek)
    #bunu yaptık çünkü hsv üzerinden değerleri almış olduk
    bitwise=cv2.bitwise_and(kare,kare,mask=mask)
    #bu işlemin orijinal resmi ile bitwise_and olarak yaptığımızda renk kazanır çünkü siyah 0 dır ve and işleminde siyah baskın çıkmış olacak
    #böylece renk kısmı görünür
    cv2.imshow("hsv",hsv)
    cv2.imshow("kare",kare)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)
    if cv2.waitKey(25) & 0xFF == ord("f"):
        break
kamera.release()
cv2.destroyAllWindows()
