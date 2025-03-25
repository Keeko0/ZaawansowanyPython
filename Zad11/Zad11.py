import numpy as np
import cv2


image_path = "ZaawansowanyPython/Zad11/miner.jpg"
image = cv2.imread(image_path)

def zad1():
    mask = np.zeros(image.shape[:2], dtype="uint8")

    cv2.rectangle(mask, (430, 80), (550, 225), 255, -1)

    masked = cv2.bitwise_not(image, image, mask=mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)

def zad2():
    mask = np.full(image.shape[:2],255, dtype="uint8")

    cv2.rectangle(mask, (450, 110), (535, 140), 0, -1)

    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)

def zad3():
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([60, 200, 10])
    upper_red = np.array([160, 255, 255])
    
    mask= cv2.inRange(hsv, lower_red, upper_red)

    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("T-shirt", result)
    cv2.waitKey(0)

zad3()