import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True :
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'): #nos devuelve el codigo ascii de cada letra del teclado pero si es q entonces cerramos la ventana
        break
cap.release()
cv2.destroyAllWindows()