import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Drawing the rectangle to dodge the birds
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    # Drawing rectangle to jump the cactus
    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey... Dinosaur game is about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  # Convert into greyscale image
        data = image.load() # Loads the image
        isCollide(data)
