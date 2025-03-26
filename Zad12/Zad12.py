import numpy as np
import cv2

image_path = "ZaawansowanyPython/Zad12/test.png"
image = cv2.imread(image_path)


def zad1and2():
    (B, G, R) = cv2.split(image)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.waitKey(0)

