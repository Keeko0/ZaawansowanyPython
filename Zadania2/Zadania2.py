import cv2

image_path = "ZaawansowanyPython/Zadania2/icon.png"
image = cv2.imread(image_path)
(h, w) = image.shape[:2]

def Zoom(image, h, w):
    scale_factor = 5
    resized = cv2.resize(image, (int(w * scale_factor), int(h * scale_factor)), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Zoomed", resized)
    cv2.waitKey(0)   

def Zad1():
    (b, g, r) = image[0, 0]
    print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
      
def Zad2():   
    image[h-1, w-1] = (0, 0, 255)
    
    Zoom(image, h, w)

def Zad3():
    (b, g, r) = image[h//2, w//2]
    print("Pixel at the center - Red: {}, Green: {}, Blue: {}".format(r, g, b))

def Zad4():    
    print("Input height of the pixel:")
    while(True):
        h2 = int(input())
        if(h2 >= 0 and h2 < h):
            break
        else:
            print("Selected coordinate is OOB, Try again:")
    
    print("Input width of the pixel:")     
    while(True):
        w2 = int(input())
        if(w2 >= 0 and w2 <w):
            break
        else:
            print("Selected coordinate is OOB, Try again:")

    image[h2,w2] = (0,0,0)

    Zoom(image, h, w)

def Zad5():    
    (cX, cY) = (w//2, h//2)
    image[0:cY, 0:cX] = (255, 0, 0)
    
    Zoom(image, h, w)

def Zad6():    
    (cX, cY) = (w//2, h//2)
    square_size = 5
    image[cY - square_size:cY + square_size, cX - square_size:cX + square_size] = (0, 0, 255) 

    Zoom(image, h, w)

def Zad7():   
    div = w//6
    c = h//2
        
    center = image[c - div:c + div, c - div:c + div]
    Zoom(center, h, w)

    image[c - div:c + div, c - div:c + div] = (0,0,0)
    Zoom(image, h, w)
    
def Zad8():
    Zoom(image, h, w)  
    image[15, 0:w] = (0,255,0)
    Zoom(image, h, w)
    
def Zad9():
    Zoom(image, h, w) 
    image[5:10, 5:10] = (255, 255, 255)
    Zoom(image, h, w)     

def Zad10():
    a = int(input("Podaj wys. pierwszego piksela: "))
    b = int(input("Podaj szer. pierwszego piksela: "))
    c = int(input("Podaj wys. drugiego piksela: "))
    d = int(input("Podaj szer. drugiego piksela: "))
    (b, g, r) = image[a,b]
    (b2, g2, r2) = image[c,d]
    bd, gd, rd = (b-b2, g-g2, r-r2)
    
    print("First pixel - Red: {}, Green: {}, Blue: {}".format(r, g, b))
    print("Second pixel - Red: {}, Green: {}, Blue: {}".format(r2, g2, b2))
    print("Difference - Red: {}, Green: {}, Blue: {}".format(rd,gd,bd))

def Zad11():
    hs_px1, hs_px2 = 0, 0
    brightness = 0
    hs_b, hs_g, hs_r = 0, 0, 0
    
    for px1 in range(h):
        for px2 in range(w):
            (b, g, r) = image[px1, px2]
            brightness_check = int(b) + int(g) + int(r)
            
            if brightness_check > brightness:
                brightness = brightness_check
                hs_px1, hs_px2 = px1, px2
                hs_b, hs_g, hs_r = b, g, r

    print("Brightest Pixel - Red: {}, Green: {}, Blue: {}".format(hs_r, hs_g, hs_b))
    print("Coordinates - X: {}, Y: {}".format(hs_px2, hs_px1))
    print("Final brightness: {}, with an avarage value of: {}".format(brightness, brightness/3))

#Main
