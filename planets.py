import cv2
import numpy as np  

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255),)

cv2.putText(img,
            "Mercury",
            (100,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)

cv2.putText(img,
            "Venus",
            (200,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)

cv2.putText(img,
            "Earth",
            (300,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)


cv2.putText(img,
            "Mars",
            (400,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)

cv2.putText(img,
            "Jupiter",
            (550,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)

cv2.putText(img,
            "Saturn",
            (850,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)

cv2.putText(img,
            "Uranus",
            (950,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)

cv2.putText(img,
            "Neptune",
            (1050,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255),)
cv2.imshow("output",img)
cv2.waitKey(0)


