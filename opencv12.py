import cv2
import numpy as np

x=cv2.imread("x.png")
y=cv2.imread("y.png")
print(f"X shape:{x.shape}\nY shape:{y.shape}\nx[202,150]:{x[202,150]}\ny[202,150]:{y[202,150]}\ncv2 cinsinden x+y:{cv2.add(x[202,150],y[202,150])}\nnumpy cinsinden x+y:{x[202,150]+y[202,150]}\nağırlıklı toplam x+y:{cv2.addWeighted(x[202,150],0.2,y[202,150],0.8,1)}")
toplam=cv2.add(x[202,150],y[202,150])
agırlıklıtoplam=cv2.addWeighted(x[202,150],0.2,y[202,150],0.8,1)
cv2.imshow("toplam",toplam)
cv2.imshow("ağırlıklıtoplam",agırlıklıtoplam)
cv2.imshow("x",x)
cv2.imshow("y",y)
cv2.waitKey(0)
cv2.destroyAllWindows()

