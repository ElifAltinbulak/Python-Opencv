import cv2
import numpy as np
resim=cv2.imread("images.jfif")
#görüntüyü iki katına çıkarmak ve iki katına düşürmek birer görüntü piramitleridir
iki_kat=cv2.pyrUp(resim)
iki_kat_düşürme=cv2.pyrDown(resim)
print(f"Orijinal={resim.shape}\nİki kat={iki_kat.shape}\nİki kat düşürme={iki_kat_düşürme.shape}")
#shapelerin iki katına çıktığını görmüş bulumaktayız
cv2.imshow("resim",resim)
cv2.imshow("iki kat",iki_kat)
cv2.imshow("iki kat düşürme",iki_kat_düşürme)
#diyelim ki çalışman gereken resim küçük bir resim o zaman yapılması gereken var olan resmi küçültmek ya da büyütme işlemlerini yaparak
#daha rahat bir şekilde kullanılabilir
cv2.waitKey(0)
cv2.destroyAllWindows()
