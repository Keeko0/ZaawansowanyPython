import cv2
import os
import numpy as np

image= cv2.imread(os.path.join(os.path.dirname(__file__), "kurka.jpg"))
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)   
h, s, v = cv2.split(hsv)

def Zad1():
    cv2.imshow("1", image_rgb)

    b, g, r = cv2.split(image)
    cv2.imshow("2", b)
    cv2.imshow("3", g)
    cv2.imshow("4", r)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("5", hsv)

    h, s, v = cv2.split(hsv)
    cv2.imshow("6", h)
    cv2.imshow("7", s)
    cv2.imshow("8", v)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad2():
    
    s2 = cv2.add(s, 30)
    modified_hsv = cv2.merge([h, s2, v])
    modified_bgr = cv2.cvtColor(modified_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("1", image)
    cv2.imshow("2", modified_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad3():
    lower_blue = np.array([100, 100, 50])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("1", image)
    cv2.imshow("2", mask)
    cv2.imshow("3", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad4():
    h2 = (h + 30) % 180
    shifted = cv2.merge([h2, s, v])
    result = cv2.cvtColor(shifted, cv2.COLOR_HSV2BGR)

    cv2.imshow("1", image)
    cv2.imshow("2", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad5():
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("1", image)
    cv2.imshow("2", mask)
    cv2.imshow("3", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad6():
    lower_skin = np.array([0, 20, 70])
    upper_skin = np.array([25, 255, 255])
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("1", image)
    cv2.imshow("2", mask)
    cv2.imshow("3", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad7():
    lower_s = cv2.subtract(s, 100)
    hsv_lower = cv2.merge([h, lower_s, v])
    img_lower = cv2.cvtColor(hsv_lower, cv2.COLOR_HSV2BGR)

    higher_s = cv2.add(s, 100)
    hsv_higher = cv2.merge([h, higher_s, v])
    img_higher = cv2.cvtColor(hsv_higher, cv2.COLOR_HSV2BGR)

    cv2.imshow("1", image)
    cv2.imshow("2", img_lower)
    cv2.imshow("3", img_higher)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad8():
    red1 = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
    red2 = cv2.inRange(hsv, (160, 100, 100), (179, 255, 255))
    red = cv2.bitwise_or(red1, red2)

    green = cv2.inRange(hsv, (35, 40, 40), (85, 255, 255))
    blue = cv2.inRange(hsv, (100, 100, 50), (140, 255, 255))

    combined_mask = cv2.bitwise_or(red, cv2.bitwise_or(green, blue))
    result = cv2.bitwise_and(image, image, mask=combined_mask)

    cv2.imshow("1", image)
    cv2.imshow("2", combined_mask)
    cv2.imshow("3", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Zad1()