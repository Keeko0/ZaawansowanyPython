import numpy as np
import cv2

def zad1():
    image = np.ones((300, 300, 3), np.uint8) * 0  

    pt1 = (150, 10)
    pt2 = (10, 290)
    pt3 = (290, 290)
    triangle = np.array([pt1, pt2, pt3])
    cv2.drawContours(image, [triangle], 0, (255, 255, 255), -1)

    circle = np.zeros((300, 300, 3), dtype="uint8")
    cv2.circle(circle, (150, 150), 150, (255, 255, 255), -1)

    and_ = cv2.bitwise_and(image, circle)
    or_ = cv2.bitwise_or(image, circle)
    not_ = cv2.bitwise_not(image)
    xor_ = cv2.bitwise_xor(image,circle)

    cv2.imshow("and", and_)
    cv2.imshow("or", or_)
    cv2.imshow("not", not_)
    cv2.imshow("xor", xor_)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad2():
    image_path1 = "ZaawansowanyPython/Zadania10/test1.png"
    image1 = cv2.imread(image_path1)

    image_path2 = "ZaawansowanyPython/Zadania10/test2.png"
    image2 = cv2.imread(image_path2)

    xor_ = cv2.bitwise_xor(image1,image2)
    
    cv2.imshow("1", image1)
    cv2.imshow("2", image2) 
    cv2.waitKey(0)  
       
    cv2.imshow("xor", xor_)
    cv2.waitKey(0)

zad2()