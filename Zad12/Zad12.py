import numpy as np
import cv2
import os

image = cv2.imread(os.path.join(os.path.dirname(__file__), "test.png"))
img2 = cv2.imread(os.path.join(os.path.dirname(__file__), "miner.jpg"))
logo = cv2.imread(os.path.join(os.path.dirname(__file__), "logo.png"))

def zad1and2():
    (B, G, R) = cv2.split(image)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.waitKey(0)

def zad3():
    (B, G, R) = cv2.split(image)
    merged = cv2.merge([R, G, B])
    cv2.imshow("Merged", merged)
    cv2.imshow("Normal", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad4():
    (B, G, R) = cv2.split(image)
    R = cv2.add(R, -100) #used negative value intead, as the value is already set as 255
    merged = cv2.merge([B, G, R])
    cv2.imshow("Merged", merged)
    cv2.imshow("Normal", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad5():
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([60, 200, 10])
    upper_red = np.array([160, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(img2, img2, mask=mask)
    
    b, g, r = cv2.split(result)
    r = cv2.add(r, 255)
    b = cv2.add(b, 50)
    g = cv2.add(g, -255)
    result = cv2.merge((b, g, r))
    
    final = img2.copy()
    final[mask > 0] = result[mask > 0]
    
    cv2.imshow("Bluer T-shirt", final)
    cv2.imshow("OG",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad6():
    (B, G, R) = cv2.split(logo)
    G = cv2.add(G, -255)
    merged = cv2.merge([R, G, B])
    cv2.imshow("Merged", merged)
    cv2.imshow("Normal", logo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
zad5()
