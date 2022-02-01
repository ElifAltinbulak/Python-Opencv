import cv2
import numpy as np
#kamera kayıt
def Main():
    kamera=cv2.VideoCapture(0)
    fourcc=cv2.VideoWriter_fourcc(*"mp4v")
    kayit=cv2.VideoWriter("kayit.mp4",fourcc,30,(640,540))
    while True:
        ret,goruntu=kamera.read()
        if ret==True:
            kayit.write(goruntu)
        cv2.imshow("Görüntü",goruntu)
        if cv2.waitKey(25) & 0xFF == ord("f"):
            break
    kamera.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    Main()
