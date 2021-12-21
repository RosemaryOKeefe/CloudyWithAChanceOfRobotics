import cv2
import numpy as np
from PIL import Image
import pytesseract

import time
from datetime import datetime
presentime = datetime.now()
#setting height, witdt, and fps
cam=cv2.VideoCapture(0)
width=1280
height=720
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

presentime = datetime.now()
count = 0
timeStamp=time.time()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    ignore, img = cam.read()
    #making image from webcam be gray to help read
    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', grayFrame)
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)

    substring = "Protein"
    result = text.find(substring)

    if(result == -1):
        print("Given substring not found.")

    else:
        print("substring found at index : ", result)
        print("Servo will press the screen")
    if cv2.waitKey(1)==ord('q'):
        break 
cam.release
cv2.destroyAllWindows