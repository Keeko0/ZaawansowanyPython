import cv2
import os

image_path = "ZaawansowanyPython/imagePython.jpg" #Samo "picturepython.jpg" nie chciało działać na moim komputerze.
image_path2 = "ZaawansowanyPython/imageBlack.jpg"

#Zadanie1
def Zad1():
    image = cv2.imread(image_path)
    if image is None:
        print("Błąd wczytywania obrazu")
    else:
        print("Obraz wczytano poprawnie.")

        cv2.imshow("Wyświetlony obraz", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#Zadanie2
def Zad2():
    image = cv2.imread(image_path)
    (c) = image.shape[2]
    print(f'channels: {c}')

    if image is None:
        print("Błąd wczytywania obrazu")
    else:
        print("Obraz wczytano poprawnie, liczba kanałów:")
        print()

        cv2.imshow("Wyświetlony obraz", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def Zad3():
    image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Obraz w skali szarości", image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zad4():
    image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image_gray is None:
        print("Błąd wczytywania obrazu")
        return

    cv2.imshow("Obraz w skali szarości", image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_dir = "/ZaawansowanyPython"
    save_path = os.path.join(save_dir, "imageBlack.jpg")
    
    cv2.imwrite(save_path, image_gray)

def Zad5():
    image1 = cv2.imread(image_path)
    if image1 is None:
        print("Błąd wczytywania obrazu 1")
    else:
        print("Obraz 1 wczytano poprawnie.")

    image2 = cv2.imread(image_path2)
    if image2 is None:
        print("Błąd wczytywania obrazu 2")
    else:
        print("Obraz 2 wczytano poprawnie.")
        
        cv2.imshow("Wyświetlony obraz", image1)        
        cv2.imshow("Wyświetlony obraz2", image2)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def Zad6():
    image = cv2.imread(image_path)

    if image is None:
        print("Błąd wczytywania obrazu")
        return
    
    image_resized = cv2.resize(image, (1920, 1080))

    cv2.imshow("Obraz 1920x1080", image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Main