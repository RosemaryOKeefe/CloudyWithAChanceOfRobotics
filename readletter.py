import cv2
import numpy as np
from PIL import Image
import pytesseract
#from adafruit_servokit import ServoKit

import time
from datetime import datetime

#myKit = ServoKit(channels=16)
presentime = datetime.now()
cam=cv2.VideoCapture(1)
count = 0
timeStamp=time.time()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    ret, img = cam.read()
    #img = cv2.flip(img,-1)
    #cv2.imshow("Test", img)
    #img = cv2.imread('/home/Downloads/skipEng.jpeg')
    #skipROI = img[367:396, 711:800]
    #gray = cv2.cvtColor(skipROI, cv2.COLOR_BGR2GRAY)
    #ret, bw = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('image', img)
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)

    substring = "calories"
    result = text.find(substring) #start index, last index
    

    if(result == -1):
        print("Given substring not found.")
        #myKit.servo[2].angle=0
        print('servo 2 to angle 0')

    else:
        print("substring found at index : ", result)
        print("Servo will press the screen")
        '''
        for n in range(2):
            #myKit.servo[2].angle=135
            print('servo 2 to angle 135')
            time.sleep(0.2)
            #myKit.servo[2].angle=90
            print('servo 2 to angle 90')
            time.sleep(0.2)
        '''
    if cv2.waitKey(1)==ord('q'):
        break 
cam.release
cv2.destroyAllWindows
