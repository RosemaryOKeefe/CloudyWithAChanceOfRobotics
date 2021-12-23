import cv2
import numpy as np
from PIL import Image
from numpy.core.fromnumeric import size
import pytesseract
#from adafruit_servokit import ServoKit


import time
from datetime import datetime

from pytesseract.pytesseract import image_to_alto_xml

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#myKit = ServoKit(channels=16)
presentime = datetime.now()
timeStamp=time.time()

img = cv2.imread('NutritionData/BlackBeansNutritionLabel.jpg')
skipROI = img[400:50, 950:1300]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, bw = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
cv2.rectangle(img, (400,50), (950,1300), (0,255,0), 1)
cv2.imshow('image', img)
#cv2.imshow('ROI', skipROI)

text = pytesseract.image_to_string(bw, lang='eng')
print(text)



#sentence = "Skip Ad"
substring = "Calories"

def SearchString(substring):
    result = text.find(substring) #start index, last index
    if(result == -1):
        print("Given substring not found.")
        for n in range(2):
            #myKit.servo[2].angle=0
            time.sleep(0.2)
            #myKit.servo[2].angle=90 
            time.sleep(0.2) 
    else:
        print("substring found at index : ", result)
        print("Servo will press the screen")
        for n in range(2):
            #myKit.servo[0].angle=90
            time.sleep(1)
            #myKit.servo[0].angle=0
            time.sleep(1) 

SearchString(substring)
cv2.waitKey(0)
#resizing an image

resized_Img = img.resize((128,720)) 
