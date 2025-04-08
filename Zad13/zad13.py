import cv2
import os

image = cv2.imread(os.path.join(os.path.dirname(__file__), "geo.png"))
image2 = cv2.imread(os.path.join(os.path.dirname(__file__), "salted.png"))
image3 = cv2.imread(os.path.join(os.path.dirname(__file__), "steve.png"))
image4 = cv2.imread(os.path.join(os.path.dirname(__file__), "bill.jpg"))

kernel_size = (3,3)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def zad1():
    eroded = cv2.erode(gray.copy(), cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size), iterations=1)
    cv2.imshow("Rect", eroded)

    eroded2 = cv2.erode(gray.copy(), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size), iterations=1)
    cv2.imshow("Elipse", eroded2)
    cv2.waitKey(0)

def zad2():
    dilated = cv2.dilate(gray.copy(), cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size), iterations=1)
    cv2.imshow("Rect", dilated)

    dilated2 = cv2.dilate(gray.copy(), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size), iterations=1)
    cv2.imshow("Elipse", dilated2)
    cv2.waitKey(0)

def zad3():
    cv2.destroyAllWindows()
    cv2.imshow("Original", image2)
    kernelSizes = [(3, 3), (5, 5), (7, 7)]
    
    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        image13 = cv2.morphologyEx(image2, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), image13)
        cv2.waitKey(0)

def zad4():
    cv2.destroyAllWindows()
    cv2.imshow("Original", image3)
    kernelSizes = [(3, 3), (5, 5), (7, 7)]
    
    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        closing = cv2.morphologyEx(image3, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("Closing: ({}, {})".format(
        kernelSize[0], kernelSize[1]), closing)
        cv2.waitKey(0)                      

def zad5():
    ribbit = (5,5)
    picrel = image
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ribbit)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ribbit)
        
    mumbojumbo = cv2.morphologyEx(cv2.morphologyEx(cv2.morphologyEx(cv2.dilate(cv2.erode(picrel, kernel), kernel), cv2.MORPH_OPEN, kernel),cv2.MORPH_CLOSE, kernel),cv2.MORPH_GRADIENT, kernel)
    mumbojumbo2 = cv2.morphologyEx(cv2.morphologyEx(cv2.morphologyEx(cv2.dilate(cv2.erode(picrel, kernel2), kernel2), cv2.MORPH_OPEN, kernel2),cv2.MORPH_CLOSE, kernel2),cv2.MORPH_GRADIENT, kernel2)
    
    cv2.imshow("mumbojumbo", mumbojumbo)
    cv2.imshow("mumbojumbo2", mumbojumbo2)
    cv2.waitKey(0)

def zad6():
    ribbit = (2, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ribbit)

    ycrcb = cv2.cvtColor(image4, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)

    y = cv2.morphologyEx(y, cv2.MORPH_OPEN, kernel)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    y = clahe.apply(y)

    blurred = cv2.GaussianBlur(y, (3, 3), 0)
    y = cv2.addWeighted(y, 1.2, blurred, -0.2, 0)

    enhanced_ycrcb = cv2.merge((y, cr, cb))
    enhanced_color = cv2.cvtColor(enhanced_ycrcb, cv2.COLOR_YCrCb2BGR)

    cv2.imshow("Original", image4)
    cv2.imshow("Enhanced Color", enhanced_color)
    
    cv2.waitKey(0)

zad6()
    