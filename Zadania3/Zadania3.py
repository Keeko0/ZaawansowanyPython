import numpy as np
import cv2

sq_size = 300
canvas = np.zeros((sq_size, sq_size, 3), dtype="uint8")
image_path = "ZaawansowanyPython/Zadania3/zajecias.png"
image = cv2.imread(image_path)

green = (0, 255, 0)
blue = (255, 0, 0)
red = (0, 0, 255)

def Show(pic=canvas):
    scale_factor = 2
    resized = cv2.resize(pic, (int(sq_size * scale_factor), int(sq_size * scale_factor)), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Zoomed", resized)
    cv2.waitKey(0)

#Zadania
def Zad1():    
    cv2.line(canvas, (sq_size//2, sq_size//2), (sq_size, sq_size), blue,2)
    Show()

def Zad2(): #zostawilem roziary 300x300 zeby nie komplikowac
    cv2.rectangle(canvas, (0, 0), (100, 50), green,-1)
    cv2.rectangle(canvas, (int(sq_size)-3, int(sq_size)-3), (int(sq_size)-100, int(sq_size)-200), red,3)
    Show()
    
def Zad3():
    r = 40
    cv2.circle(canvas, (r,r), r, blue)
    cv2.circle(canvas, (sq_size//2, sq_size//2), 60, red)
    Show()

def Zad4():
    rec_size = 100
    cv2.rectangle(canvas, (sq_size//2 - rec_size//2, sq_size//2 - rec_size//2), (sq_size//2 + rec_size//2, (sq_size//2 + rec_size//2)), green)
    cv2.circle(canvas, (sq_size//2, sq_size//2), 30, red)    
    Show()

def Zad5():
    for r in range(0, sq_size, 20):
        if r % 60 == 0:
            color = blue
        elif r % 40 == 0:
            color = red
        else:
            color = green
        cv2.rectangle(canvas, (sq_size//2 - r//2, sq_size//2 - r//2), (sq_size//2 + r//2, (sq_size//2 + r//2)), color)
    Show()

def Zad6():
    cv2.circle(image, (135, 338), 25, red, -1)
    cv2.circle(image, (245, 345), 25, red, -1)
    cv2.circle(image, (695, 270), 20, red, -1)
    cv2.circle(image, (775, 240), 20, red, -1)
    
    cv2.rectangle(image, (150,450),(225, 515), green, -1)
    cv2.rectangle(image, (725,350),(800, 400), green, -1)
    
    cv2.circle(image,(185,360), 200, blue, 3)
    cv2.circle(image,(750,275), 175, blue, 3)
    
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    
#Main
Zad6()