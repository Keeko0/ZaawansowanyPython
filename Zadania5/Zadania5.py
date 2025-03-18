import argparse
import imutils
import cv2
import os

image_path = "ZaawansowanyPython/Zadania5/1.png"
image = cv2.imread(image_path)
(h, w) = image.shape[:2]

def Zoom(image, h, w):
    scale_factor = 3
    resized = cv2.resize(image, (int(w * scale_factor), int(h * scale_factor)), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Zoomed", resized)
    cv2.waitKey(0) 

def Zad1():
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    Zoom(image, h, w)
    Zoom(rotated, h, w)
    
def Zad2():
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    Zoom(rotated, h, w)
    
def Zad3():
    M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    Zoom(rotated, h, w)

def Zad4():
    (cX, cY) = (w // 2, h // 2)
    degree = int(input("Podaj kat: "))   
    M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    Zoom(rotated, h, w)

def Zad5():
    rotated = imutils.rotate(image, 180)
    Zoom(rotated,h, w)

def Zad6():
    rotated = imutils.rotate_bound(image, -33)
    Zoom(rotated,h, w)

def Zad7():
    print("Wynik jest taki sam")

def Zad8():
    rotated = imutils.rotate_bound(image, 30)
    rotated1 = imutils.rotate_bound(rotated, 30)
    rotated2 = imutils.rotate_bound(rotated1, 30)
    
    rotated90 = imutils.rotate_bound(image, 90)

    Zoom(rotated2,h,w)
    Zoom(rotated90,h,w)
    
    #pomniejsza sie poprzez obracanie uzywajac imutils

def Zad9():
    rotated = imutils.rotate_bound(image, 75)
    Zoom(rotated, h, w)
       
    save_dir = "ZaawansowanyPython\Zadania5"
    save_path = os.path.join(save_dir, "rotated.jpg")

    cv2.imwrite(save_path, rotated)

def Zad10():
    for kat in range(0, 360, 15):
        rotated = imutils.rotate_bound(image, kat)
        Zoom(rotated,h,w)       

#main
Zad10()