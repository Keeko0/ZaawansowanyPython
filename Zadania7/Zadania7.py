import cv2

image_path = "ZaawansowanyPython/Zadania7/1.png"
image = cv2.imread(image_path)

def printPng(flipped):
    cv2.imshow("Flipperinho", flipped)
    cv2.waitKey(0)   

def Zad1():
    flipped = cv2.flip(image, -1)
    printPng(flipped)

def Zad2():
    cv2.imshow("og", image)
    flipped = cv2.flip(image, 0)
    printPng(flipped)   

def Zad3():
    flipped = cv2.flip(image, -1)
    printPng(flipped)  

def Zad4():
    Zad1()
    Zad2()
    Zad3() 

def Zad5():   
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    fragment = image[0:cY, 0:cX].copy()
    flipped_fragment = cv2.flip(fragment, 0)
    image[0:cY, 0:cX] = flipped_fragment

    printPng(image)

def Zad6():
    input1 = int(input("Choose your flip: 1, 0, -1"))
    flipped = cv2.flip(image, input1)
    printPng(flipped)     

Zad6()