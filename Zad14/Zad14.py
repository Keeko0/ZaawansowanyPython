import cv2
import os

image = cv2.imread(os.path.join(os.path.dirname(__file__), "dingdong.png"))

def zad1():
    kernel_size = 5
    
    blurred = cv2.blur(image, (kernel_size, kernel_size))
    blurred2 = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    blurred3 = cv2.medianBlur(image, kernel_size)
    blurred4 = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Average", blurred)
    cv2.imshow("Gaussian", blurred2)
    cv2.imshow("Median", blurred3)
    cv2.imshow("Bilateral", blurred4)
    
    cv2.waitKey(0)

zad1()