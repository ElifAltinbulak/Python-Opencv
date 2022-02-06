import cv2
import numpy as np
resim=np.zeros((400,400,3),"uint8")
print(resim)
#np.zeros() diyerek yapılmış ve hepsi birer 0 lık matrixlerden oluşur
#0 lık matrixlerden oluştuğu için siyah rengini alacaktır.
resim.fill(255)
print(resim)
#.fill(255) diyerek 0 lık matrixi 255 yapmış oluruz böylece beyaz rengini de almış olacaktır
#.fill kullanarak 255 yaparak beyaz haline getirmiş oluruz 


cv2.imshow("zeros resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
