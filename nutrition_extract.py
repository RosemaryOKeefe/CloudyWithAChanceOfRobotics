#####################################
# 1/15/2022 : Updated the code to add database output, all file names are added in string
####################################
import re
from re import M
from typing import Dict
import cv2
from numpy.core.fromnumeric import resize
import pytesseract
from pytesseract import pytesseract
#import PIL
#from PIL import Image
import csv
import PIL.Image
from pytesseract import Output
from re import search
import numpy as np
import os.path
from tkinter import *
import tkinter.messagebox


#######################################
# All file names and database names
#######################################
#db_name =r'C:\Users\12086\Documents\python\data\Output_db.csv'
db_name = r'/home/pi/Desktop/code/data/Output_db.csv'
img_name = 'data/GB2.jpg'
#img_name = 'data/image.jpg'
img_name_save = 'data/image_box.jpg'


#def count(x):
#    length = len(x)
#    numbers = 0
#    letters = 0
#    space = 0
#    other = 0
#    numbers = sum(c.isdigit() for c in x)
#    letters = sum(c.isalpha() for c in x)
#    spaces  = sum(c.isspace() for c in x)
#    other  = len(x) - numbers - letters - spaces
#
#    print ("length,letters,numbers,space,other",x,length,letters,numbers,space,other)
#    return length,letters,numbers,space,other

#######################################
## Sub-function in python
# Coverts to Grams
#######################################
def Tkmsgshow(msg):
    pop=Tk()
    pop.geometry('640x200')
    pop.config(bg="blue")
    tkinter.messagebox.showinfo("Message",str(msg))
    pop.destroy()
    return

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
            value_mg = 2
            #Tkmsgshow("No mg/gms found")
    else:
        value_mg = 1
        #Tkmsgshow("No keyword found")
        
    #print ("new value", temp_word, value_mg)
    return(value_mg)



    
    
    

#######################################
## Reading out the image
## improve quality of image
## Need to make it dynamic based on image quality and size .. To be worked on ... 
#######################################
myconfig = r'-c preserve_interword_spaces=1 --psm 11 --oem 3'


img = cv2.imread(img_name)
#img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
#img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
#img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)

#adaptive_threshold = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,85, 11 )

#height, width, _ = img.shape
#print (height, width)


###########
# Covert img to text
###########
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#invert = 255 - threshold
#img = cv2.resize(img, None, fx=1.7, fy=1.7, interpolation=cv2.INTER_CUBIC)
#data = pytesseract.image_to_string(threshold,lang='eng', config='--psm 6')
#print(data)

resize = cv2.resize(img,(640,480))
cv2.imshow('Selected Image', resize)
cv2.waitKey(1000)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img,lang='eng',config=myconfig)
your_string = text
list_of_words = your_string.split()
print (list_of_words)

#######################################
#Segmenting the label into areas of interest
#Call subroutine as same function used all time
# save the values
#######################################
fdstr = ["Protein","Fat","Carb.","Fiber","Sugars"]
l = len(fdstr)


#if all(x in list_of_words for x in fdstr):
#    print ("works")
#else:
#    Tkmsgshow("Few Keyword not found, Start again")
String_Carb = "Carbohydrate"
if "Carbohydrate" in list_of_words:
    String_Carb = "Carbohydrate"
    print ("Select Carbohydrate")
if "Carb." in list_of_words:
    String_Carb = "Carb."
    print ("Selected Carb.")    
fdstr[2] = String_Carb


x=0
while x < l:
    if fdstr[x] in list_of_words:
        print ("yes")
    else:
        Tkmsgshow("No keyword "+str(fdstr[x])+" Please Start again")
        break
    x += 1
    
next_word = list_of_words[list_of_words.index('Protein') + 1]
protein_val = ret_val(next_word)
next_word1 = list_of_words[list_of_words.index('Fat') + 1]
Fat_val = ret_val(next_word1)
next_word2 = list_of_words[list_of_words.index(String_Carb) + 1]
Carb_val = ret_val(next_word2)
next_word3 = list_of_words[list_of_words.index('Fiber') + 1]
Fiber_val = ret_val(next_word3)
next_word4 = list_of_words[list_of_words.index('Sugars') + 1]
Sugars_val = ret_val(next_word4)
#Debug Statement
# next_word_array = [next_word, next_word1, next_word2, next_word3, next_word4]

#######################################
##Label out the values of each nutrients.
#######################################
print ("Prot:", next_word,":",protein_val, "Fat:", next_word1,
       ":",Fat_val,"Carb:",next_word2,":", Carb_val,"Fiber:",
       next_word3,":",Fiber_val,"Sugar:", next_word4,":",Sugars_val)

r_String = (protein_val, Fat_val,Carb_val,Fiber_val,Sugars_val)
#Debug Statement
#cv2.imshow('img', img)
#cv2.waitKey(125)


#######################################
# Putting data from code into database
#######################################
# Add Header to the file name
r_Header = ["Protien","Fat","Carb","Fiber","Sugar","Sodium"]
if False == os.path.exists(db_name):
   with open(db_name, 'w',encoding='UTF8',newline='') as f:
      writer = csv.writer(f)  
      writer.writerow(r_Header)
#Append new data to database
with open(db_name, 'a',encoding='UTF8',newline='') as f:
   writer = csv.writer(f)
   writer.writerow(r_String)

#############################
# Display the image to user
#############################
#img = cv2.cvtColor(img, 0)
#kernel = np.ones((1, 1), np.uint8)
#img = cv2.dilate(img, kernel, iterations=1)
#img = cv2.erode(img, kernel, iterations=1)

# Code to print boxes in the Image
height, width, _ = img.shape
data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
#print (data)
amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 50:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x,y), (x+width, y+height), (0, 255, 0), 2)
        img = cv2.putText(img, data['text'][i], (x, y+height-20), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imwrite(img_name_save, img)
resize = cv2.resize(img,(640,480))
cv2.imshow('OCR Boxed Image', resize)
cv2.waitKey(3000)
cv2.destroyAllWindows()


##################################
#See if food is healthy or not in fiber
##################################
pop=Tk()
pop.geometry('640x200')
pop.config(bg="blue")
healthy_fiber = int(Fiber_val)/int(Carb_val)
fdstr = "Carb=",Carb_val,"gms | Fiber=",Fiber_val,"gms"

if healthy_fiber > 0.1:
    tkinter.messagebox.showinfo("Message","Food is rich in fiber"+str(fdstr))
    print('Food is rich in fiber.')
else:
    tkinter.messagebox.showinfo("Message","Food does not have sufficient amount of fiber "+str(fdstr))
    print('Food does not have sufficient amount of fiber.')

pop.destroy()