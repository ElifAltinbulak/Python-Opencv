import cv2 
import numpy as np

resim=cv2.imread("pempe.jfif")
#resmi uzatma
uzat=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)
#resmi aynalama
aynala=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
#resmi tekrar etme
tekrar=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
#resmi etrafına sarma
sarma=cv2.copyMakeBorder(resim,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,0,255])

cv2.imshow("Orjinal",resim)
cv2.imshow("Uzatma",uzat)
cv2.imshow("Aynalama",aynala)
cv2.imshow("Tekrar",tekrar)
cv2.imshow("Sarma",sarma)
