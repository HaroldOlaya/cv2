import cv2
import numpy as np
import mediapipe as mp

mp_drawing= mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap=cv2.VideoCapture(0)
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5)as hands:
    while True:
        ret,frame=cap.read()
        if ret == False:
            break

        height,width,_=frame.shape
        frame=cv2.flip(frame,1)
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        resultado=hands.process(frame_rgb)
        #print(resultado.multi_handedness)
        #print(resultado.multi_hand_landmarks)#ubicacion de los 21 puntos en la mano

        if resultado.multi_hand_landmarks is not None:

        #--- dibujar los puntos en la mano
            for hand_landmarks in resultado.multi_hand_landmarks:
                xpulgar=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
                ypulgar = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
                xindice=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                yindice = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
                xcorazon=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x*width)
                ycorazon = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
                puntox=int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x*width)
                puntoy=int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y*height)
                print(puntox,puntoy)
                mp_drawing.draw_landmarks(

                    frame,hand_landmarks,mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec((255,0,0),thickness=2,circle_radius=3),
                    mp_drawing.DrawingSpec((0,0,0),thickness=2)
                )

        cv2.imshow("Camara activa", frame)
        if cv2.waitKey(1) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

