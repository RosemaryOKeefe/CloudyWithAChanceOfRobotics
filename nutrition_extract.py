#####################################
# 1/15/2022 : Updated the code to add database output, all file names are added in string
# 2/10/2022 : Updated to database
# 3/01/2022 : Created subroutines and tkinter message boxes
####################################
import re
from re import M
from typing import Dict
import cv2
from numpy.core.fromnumeric import resize
import pytesseract
from pytesseract import pytesseract
import csv
import PIL.Image
from pytesseract import Output
from re import search
import numpy as np
import os.path
from tkinter import *
import tkinter.messagebox
import tkinter as tk

#######################################
# All file names and database names
#######################################
#db_name =r'C:\Users\12086\Documents\python\data\Output_db.csv' # --> Used for laptop debug
db_name = r'/home/pi/Desktop/code/data/Output_db.csv'  # --> Raspberry pi only
img_name = 'data/h.jpg' #img_name = 'data/image.jpg'
img_name_save = 'data/image_box.jpg'
img_process = 'data/img_process.jpg'


#######################################
## Sub-function in python
#######################################

# Display fixed CWACOR banner with logo
def WIP(dly, image_display):
    imgp = cv2.imread(image_display,1)
    #imgr = cv2.resize(imgp,(640,480))
    cv2.imshow('Image Processing', imgp)
    cv2.waitKey(dly)
    cv2.destroyAllWindows()
    return
# Displays messages on touch screen based on msg string
def Tkmsgshow(msg):
    pop=Tk()
    pop.geometry('640x200')
    pop.config(bg="blue")
    tkinter.messagebox.showinfo("Message",str(msg))
    pop.destroy()
    return
# Computes milligrams to Grams and extracts values
def ret_val(temp_word):
    name_cmp_mg = 'mg'
    name_cmp_g = 'g'
    value_mg = 0
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
## improve readability of the image by resizing and using cubic interpolation
## Would like to make it dynamic based on image quality and size .. To be worked on ... Need more powerful processor
#######################################
myconfig = r'-c preserve_interword_spaces=1 --psm 11 --oem 3'
img = cv2.imread(img_name)
#img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
#img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
#img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)
#adaptive_threshold = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,85, 11 )
#height, width, _ = img.shape

resize = cv2.resize(img,(640,480))
cv2.imshow('Selected Image', resize)
cv2.waitKey(5000)
cv2.destroyAllWindows()

# Covert img to text
text = pytesseract.image_to_string(img,lang='eng',config=myconfig)
your_string = text
list_of_words = your_string.split()
print (list_of_words)

######################################
WIP(1000, img_process)

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
    
######################################
WIP(1000, img_process)
######################################

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

######################################
WIP(1000, img_process)
######################################


#######################################
##Label out the values of each nutrients.
#######################################
print ("Prot:", next_word,":",protein_val, "Fat:", next_word1,
       ":",Fat_val,"Carb:",next_word2,":", Carb_val,"Fiber:",
       next_word3,":",Fiber_val,"Sugar:", next_word4,":",Sugars_val)
from datetime import datetime
dt = datetime.now()
r_String = (dt, protein_val, Fat_val,Carb_val,Fiber_val,Sugars_val)
#Debug Statement
#cv2.imshow('img', img)
#cv2.waitKey(125)


#######################################
# Putting data from code into database
#######################################
# Add Header to the file name

r_Header = ["ID","Protien","Fat","Carb","Fiber","Sugar" ]
if False == os.path.exists(db_name):
   with open(db_name, 'w',encoding='UTF8',newline='') as f:
      writer = csv.writer(f)  
      writer.writerow(r_Header)
#Append new data to database
with open(db_name, 'a',encoding='UTF8',newline='') as f:
   writer = csv.writer(f)
   writer.writerow(r_String)

f.close()

######################################
WIP(1000, img_process)

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
cv2.waitKey(5000)
cv2.destroyAllWindows()


##################################
#Check : a) food is healthy or not in fiber b) Food category
##################################
healthy_fiber = int(Fiber_val)/int(Carb_val)
if healthy_fiber > 0.1:
    healthy_val = 'Rich Fiber'
else:
    healthy_val = 'Low Fiber'
print(healthy_val)
food='Pantry Staples'
if protein_val < 8 and protein_val > 6:
    print('food is protein')
    food = 'Protein'
if Sugars_val < 45 and Sugars_val > 11:
    print('food is a Grain')
    food = 'Grain'



r_Hdr = [("Health Status"),("   ●Carb"),("   ●Fiber"),("Category"),("Database ID")] 
r_Str = [(healthy_val),(Carb_val),(Fiber_val),(food),(dt)]
 
# find total number of rows and columns 
r_matrix = [(r_Hdr[0], r_Str[0]),
            (r_Hdr[1], r_Str[1]),
            (r_Hdr[2], r_Str[2]),
            (r_Hdr[3], r_Str[3]),
            (r_Hdr[4], r_Str[4])]
        
# columns in list
total_rows = len(r_matrix)
total_columns = len(r_matrix[0])
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                #print(r_Str[i])
                self.e = Entry(root, width=17, fg='black',
                       font=('Arial',16,'bold'), bg='white', relief=GROOVE)
                #root.grid_rowconfigure(index=i, weight=0)
                if j > 0:
                    if i == 0:
                        if healthy_val == 'Rich Fiber':
                            self.e = Entry(root, width=17, fg='white',
                               font=('Arial',16,'bold'), bg='green',relief=RAISED)
                            health = 1
                        else:
                            self.e = Entry(root, width=17, fg='white',
                                font=('Arial',16,'bold'), bg='red',relief=SUNKEN)
                            health = 0                            
                    elif i == 3:
                        print('check')
                        if health == 1:
                            self.e = Entry(root, width=17, fg='white',
                                font=('Arial',16,'bold'), bg='green',relief=SUNKEN)
                        elif health == 0:
                            self.e = Entry(root, width=17, fg='white',
                                font=('Arial',16,'bold'), bg='red',relief=SUNKEN)

                self.e.grid(row=i, column=j,padx=10,pady=10, ipadx=40,sticky = 'EW')
                self.e.insert(END, r_matrix[i][j])

        tk.Button(root,text="OK", command=root.destroy, fg='yellow', font=('Arial', 16,'bold'),bg='purple').grid(row=6, column=1, padx=10,pady=10, ipadx=40,sticky = 'EW')

# create root window
root = Tk()
root.title('Nutrient Information')

t = Table(root)
#root.grid_columnconfigure(1, weight=1)
root.mainloop()


##################################
#Display : Database last few records
##################################
datadb = tk.Tk()
datadb.geometry("800x250")
datadb.resizable(width=True, height=True)
datadb.title("Database")

i=0
for i, col_name in enumerate(r_Header, start=1):
    tk.Label(datadb, text=col_name,bg='black', fg='white', font=('Arial',15,'bold')).grid(row=1, column=i, padx=10)

file1 = open(db_name, 'r')
Lines = file1.readlines()
length = len(Lines) -5
last_lines = Lines[-5:]  
count=1

# Strips the newline character
for line in last_lines:
    length += 1
    count += 1
    data = line.strip()
    cs = data.split(",")
    #print("Record{}: {}".format(length, line.strip()))
    for i, col_name in enumerate(cs, start=1):    
        tk.Label(datadb, text=col_name, fg='black', font=('Arial',15,'bold')).grid(row=count, column=i, padx=10)

file1.close()
tk.Label(datadb, text="Total Records: "+str(length), fg='blue', font=('Arial',15,'bold')).grid(row=count+1,column=1, padx=10)
tk.Label(datadb,fg='red').grid(row=count+1, column=4, padx=20)

tk.Button(datadb,text="OK", command=datadb.destroy, fg='yellow', font=('Arial', 15),bg='purple').grid(row=count+2, column=4,padx=10,pady=10, ipadx=10,sticky = 'EW')

datadb.mainloop()
