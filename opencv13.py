import cv2 
import numpy as np
kamera=cv2.VideoCapture(0)
while True:
    ret,goruntu=kamera.read()
    resim=cv2.imread("silgi.png",0)
    gri_ton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    w,h=resim.shape
    res=cv2.matchTemplate(gri_ton,resim,cv2.TM_CCOEFF_NORMED)
    esik_deger=0.5
    loc=np.where(res>esik_deger)
    for n in zip(*loc[::-1]):
        cv2.rectangle(goruntu,n,(n[0]+h,n[1]+w),(255,0,0),2)
        cv2.putText(goruntu,"Silgi",(n[0]+10,n[1]+10),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
    cv2.imshow("kamera",goruntu)
    if cv2.waitKey(25) &0xFF==ord("f"):
        break
kamera.release()
cv2.destroyAllWindows()
