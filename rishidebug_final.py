import re
from re import M
from typing import Dict
import cv2
from numpy.core.fromnumeric import resize
import pytesseract
from pytesseract import pytesseract
#import PIL
#from PIL import Image
#import csv
import PIL.Image
from pytesseract import Output
from re import search
import numpy as np

def count(x):
    length = len(x)
    numbers = 0
    letters = 0
    space = 0
    other = 0
    numbers = sum(c.isdigit() for c in x)
    letters = sum(c.isalpha() for c in x)
    spaces  = sum(c.isspace() for c in x)
    other  = len(x) - numbers - letters - spaces

    print ("length,letters,numbers,space,other",x,length,letters,numbers,space,other)
    return length,letters,numbers,space,other

## Sub-function in python
# Coverts to Grams
def ret_val(temp_word):
    name_cmp_mg = 'mg'
    name_cmp_g = 'g'
    #array_string = count(temp_word)
    if any((c in name_cmp_g) for c in temp_word):
        if sum(c.isdigit() for c in temp_word) > 0:
            res = [re.findall(r'(\d+)(\w+)', temp_word)]
            #print ("res", res, temp_word)
            number=res[0][0][0]
            name = res[0][0][1]
            if name == name_cmp_mg:
                value_mg = int(number)/1000
            else:
                value_mg = int(number)
        else:
            value_mg = -2
    else:
        value_mg = -1

    #print ("new value", temp_word, value_mg)
    return(value_mg)



## Reading out the image
## improve quality of image
## Need to make it dynamic based on image quality and size .. To be worked on ... 
myconfig = r'--psm 11 --oem 3'
img = cv2.imread('data/readme.jpg')

img = cv2.resize(img, None, fx=1.7, fy=1.7, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, 0)
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

height, width, _ = img.shape
data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 50:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        #img = cv2.rectangle(img, (x,y), (x+width, y+height), (0, 255, 0), 2)
        #img = cv2.putText(img, data['text'][i], (x, y+height-20), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 1, cv2.LINE_AA)
#cv2.imshow('img', img)
#cv2.waitKey(0)
text = pytesseract.image_to_string(img)
your_string = text
list_of_words = your_string.split()
#print (list_of_words)

#Segmenting the label into areas of interest
#Call subroutine as same function used all time
next_word = list_of_words[list_of_words.index('Protein') + 1]
protein_val = ret_val(next_word)
next_word1 = list_of_words[list_of_words.index('Fat') + 1]
Fat_val = ret_val(next_word1)
next_word2 = list_of_words[list_of_words.index('Carbohydrate') + 1]
Carb_val = ret_val(next_word2)
next_word3 = list_of_words[list_of_words.index('Fiber') + 1]
Fiber_val = ret_val(next_word3)
next_word4 = list_of_words[list_of_words.index('Sugars') + 1]
Sugars_val = ret_val(next_word4)
next_word5 = list_of_words[list_of_words.index('Sodium') + 1]
sodium_val = ret_val(next_word5)

#Debug Statement
# next_word_array = [next_word, next_word1, next_word2, next_word3, next_word4]

##Label out the values of each nutrients.
print ("Prot:", next_word,":",protein_val, "Fat:", next_word1,":",Fat_val,"Carb:",next_word2,":", Carb_val,"Fiber:", next_word3,":",Fiber_val,"Sugar:", next_word4,":",Sugars_val,"Sodium:",next_word5,":",sodium_val )

#Debug Statement
#cv2.imshow('img', img)
#cv2.waitKey(0)