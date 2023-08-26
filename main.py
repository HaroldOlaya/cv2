import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True :
    ret,frame = cap.read()
    width= int(cap.get(3))
    height=int(cap.get(4))

    img=cv2.line(frame,(0,0),(width,height),(0,0,0),8)#trazando una linea en la pantalla
    img = cv2.rectangle(img, (100,100),(300,300),(0,0,255),1)# creamos un rectangulo en la pantalla
    img =cv2.circle(img,(350,350),60,(0,255,0),2) # creamos un circulo en la pantalla
    font = cv2.FONT_HERSHEY_SIMPLEX# definiendo el tipo de texto
    IMG =cv2.putText(img,'Harold',(10,height-10),font,2,(255,255,255),5,cv2.LINE_AA)#colocandole texto a la imagen
    cv2.imshow('frame',img)
    if cv2.waitKey(1) == ord('q'): #nos devuelve el codigo ascii de cada letra del teclado pero si es q entonces cerramos la ventana
        break
cap.release()
cv2.destroyAllWindows()