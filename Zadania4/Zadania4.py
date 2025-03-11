import cv2
import numpy as np
import imutils as im


image_path = "ZaawansowanyPython/Zadania4/1.png"
image = cv2.imread(image_path)

def Zad1_2_3():
    cv2.imshow("Normal", image)
    cv2.waitKey(0)
    
    #1
    M = np.float32([[1, 0, 30], [0, 1, 40]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    cv2.imshow("Shifted", shifted)
    cv2.waitKey(0)

    #2
    M2 = np.float32([[1, 0, -20], [0, 1, -50]])
    shifted2 = cv2.warpAffine(shifted, M2, (shifted.shape[1], shifted.shape[0]))

    cv2.imshow("ShiftedTwice", shifted2)
    cv2.waitKey(0)

    #3
    M3 = np.float32([[1, 0, 100], [0, 1, 0]])
    shifted3 = cv2.warpAffine(image, M3, (image.shape[1], image.shape[0]))

    cv2.imshow("ShiftedOnce", shifted3)
    cv2.waitKey(0)

def Zad4():
    shifted = im.translate(image, 100, 50)
    cv2.imshow("Shifted Down", shifted)
    cv2.waitKey(0)

def Zad5():
    tx = int(input("Podaj tX: "))
    ty = int(input("Podaj tY: "))
    shifted = im.translate(image, tx, ty)
    cv2.imshow("Shifted Down", shifted)
    cv2.waitKey(0)

#main




