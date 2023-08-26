import cv2
import numpy as np
import mediapipe as mp

mp_drawing= mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5)as hands:

    image = cv2.imread('assets/mano.png')
    height,width,_=image.shape
    image=cv2.flip(image,1)
    image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    resultado=hands.process(image_rgb)
    #print(resultado.multi_handedness)
    #print(resultado.multi_hand_landmarks)#ubicacion de los 21 puntos en la mano
    if resultado.multi_hand_landmarks is not None:
        #--- dibujar los puntos en la mano
        #for hand_landmarks in resultado.multi_hand_landmarks:
        #    print(hand_landmarks)
        #    mp_drawing.draw_landmarks(
        #        image,hand_landmarks,mp_hands.HAND_CONNECTIONS,
        #        mp_drawing.DrawingSpec((255,0,0),thickness=2,circle_radius=3),
        #        mp_drawing.DrawingSpec((0,0,0),thickness=2)
        #    )
        #--------- segunda manera de obtener los dedos
        #for hand_landmarks in resultado.multi_hand_landmarks:# aca vamos a acceder a las puntas de los dedos
        #    xpulgar=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
        #    ypulgar = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
        #    print(xpulgar,ypulgar)
        #    xindice=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
        #    yindice = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
        #    print(xindice,yindice)
        #    cv2.circle(image,(xpulgar,ypulgar),4,(255,0,0))
        #    cv2.circle(image, (xindice, yindice), 4, (255, 0, 0))


cv2.imshow("Mano",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

