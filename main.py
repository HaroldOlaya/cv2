import cv2
import numpy as np

img = cv2.imread('assets/tablero.png')
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
esquinas = cv2.goodFeaturesToTrack(gray,100,0.01,10)
esquinas = np.int0(esquinas)

for esquina in esquinas:
    x,y = esquina.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),1)
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()