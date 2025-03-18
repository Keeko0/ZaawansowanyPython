import cv2
import imutils
import os

image_path = "ZaawansowanyPython/Zadania6/1.png"
image = cv2.imread(image_path)

def printPng(resized):
    cv2.imshow("xd", resized)
    cv2.waitKey(0)
    
def Zad1():
    resized = imutils.resize(image, width=int(image.shape[1] / 2), inter=cv2.INTER_AREA)
    printPng(resized)

def Zad2():
    resized = imutils.resize(image, width=image.shape[1] * 2, inter=cv2.INTER_LINEAR)
    printPng(resized)

def Zad3():
    resized = cv2.resize(image, (200, 300), interpolation=cv2.INTER_AREA)
    printPng(resized)

def Zad4():
    methods = [
        ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
        ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
        ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
        ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

    for (name, method) in methods:
        print("[INFO] {}".format(name))
        resized = imutils.resize(image, width=image.shape[1] * 3,
        inter=method)
        cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)

def Zad5():
    resized = imutils.resize(image, width=500, inter=cv2.INTER_NEAREST)
    printPng(resized)

def Zad6():
    resized = imutils.resize(image, height=400, inter=cv2.INTER_NEAREST)
    printPng(resized)

def Zad7():
    resized = imutils.resize(image, width=int(image.shape[1] / 5), inter=cv2.INTER_AREA)
    printPng(resized)
    
    resized2 = imutils.resize(image, width=int(image.shape[1] / 5), inter=cv2.INTER_LINEAR)
    printPng(resized2)

def Zad8():
    resized = imutils.resize(image, width=500, inter=cv2.INTER_CUBIC)
    printPng(resized)
    
    resized2 = imutils.resize(image, width=500, inter=cv2.INTER_LANCZOS4)
    printPng(resized2)
    
def Zad9():
    for resize in range(10, 30, 2):
        resized = imutils.resize(image, width=int(image.shape[1] * (resize/10)), inter=cv2.INTER_AREA)
        cv2.imshow("xd", resized)
        cv2.waitKey(500)

def Zad10():
    resized = imutils.resize(image, width=800, inter=cv2.INTER_CUBIC)
    printPng(resized)
    
    save_dir = "ZaawansowanyPython\Zadania6"
    save_path = os.path.join(save_dir, "rotated.jpg")

    cv2.imwrite(save_path, resized)
    
Zad10()
