import cv2

image_path = "ZaawansowanyPython/Zadania8/1.jpg"
image = cv2.imread(image_path)
(h, w) = image.shape[:2]

def printPng(roi):
    cv2.imshow("roi", roi)
    cv2.waitKey(0)   
    
def Zad1():
    roi = image[0:100, 0:100]
    printPng(roi)

def Zad2():
    roi1 = image[0:int(h/2), 0:w]
    roi2 = image[int(h/2):h, 0:w]
    printPng(roi2)

def Zad3():
    roi = image[0:h, int(w/2):w]
    printPng(roi)

def Zad4():
    startX = int(input("startX:"))
    endX = int(input("endX:"))
    startY = int(input("startY:"))
    endY = int(input("endY:"))
    
    roi = image[startY:endY, startX:endX]
    printPng(roi)

def Zad5():
    roi = image[0:200, 200:400]
    printPng(roi)   

def Zad6():
    roi = image[50:150, 250:350].copy()
    image[300:400, 400:500]= roi

    printPng(image)

def Zad7():
    rois = [
        image[0:int(h/3), 0:int(w/3)],
        image[0:int(h/3), int(w/3):(int(w/3)*2)],   
        image[0:int(h/3), int((w/3)*2):w],      
        image[int(h/3):(int(h/3)*2), 0:int(w/3)],   
        image[int(h/3):(int(h/3)*2), int(w/3):(int(w/3)*2)], 
        image[int(h/3):(int(h/3)*2), int((w/3)*2):w],     
        image[(int(h/3)*2):h, 0:int(w/3)],     
        image[(int(h/3)*2):h, int(w/3):(int(w/3)*2)],     
        image[(int(h/3)*2):h, int((w/3)*2):w]                 
    ]
    for roi in rois:
        printPng(roi)

def Zad8():
    move = 50
    for x in range(move, w-move, move):
        roi2 = image[0:h, x-move:x+move]
        printPng(roi2)    

Zad8()