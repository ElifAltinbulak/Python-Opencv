import cv2
import numpy as np
#biz genelde bir resim üzerinde çalıştık ama boş bir pencere üstünde çalışmadık
#çalışacağımız alan sadece resim olmak zorunda değil kendi belirlediğimiz bir
#görüntüde de çalışabiliriz.
#bunun için bizler numpy arraylerinde bir boş alan yapabiliriz
#tek tek yapabiliriz ama tek tek np array yazmak zaman kaybıdır
#bunun için numpy kütüphanesinde bulunan np.zeros() methodunu kullanmalıyız bu
#method bize belirli bir alanı boş çıkarıp isteğidiğimiz şekilde kullanmamızı sağlayacaktır
boş_alan=np.zeros((400,400,3),dtype="uint8")
#tuple içine yazılır sakın unutma
cv2.rectangle(boş_alan,(300,100),(100,300),(255,255,255))
cv2.imshow("kalan kısım",boş_alan)
