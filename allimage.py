import sys
import os
import cv2
import cv2
import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

###################################
# Creating paths and define ints
###################################
imagename = "data/image.jpg"


###################################
# Subroutines
###################################

# Calls other file
def run():
    os.system('python nutrition_extract.py')
    
# Captures image samples    
def webcapture():
    TIMER = int(5)
    #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap = cv2.VideoCapture(0)
    
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)# 0= Off, 1 = On
    #cap.set(3, 1280) #set width to 1280
    #cap.set(4, 720) #set height to 720
    
    while True:
        ret, img = cap.read()
        
        prev = time.time()
        while TIMER >= 0:
            ret, img = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(TIMER),
                            (200, 250), font,
                            7, (0, 255, 255),
                            4, cv2.LINE_AA)
            cv2.imshow('Camera', img)
            cv2.waitKey(125)
            cur = time.time()
            if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
            else:
                ret, img = cap.read()
                cv2.imshow('Camera', img)
                cv2.waitKey(125)
                cv2.imwrite(imagename, img)
        # close the camera
        cap.release()
        # close all the opened windows
        cv2.destroyAllWindows()
        
        run()

        return(imagename)

###################################
# Main Function - Python tkinter
###################################
window=Tk()
window.title("Running Python Script")
window.geometry("500x500")#('1080x720')
window.attributes('-fullscreen', True)
myFont = tkFont.Font(family='Helvetica',size=18)
w = 38
h = 25

btn = Button(window, text="Start", bg="green", fg="white",command=webcapture,width=w,height=h)
btn.grid(column=0, row=0)
btn['font'] = myFont

btn3 = Button(window, text="Stop", bg="red", fg="white",command=exit,width=w,height=h)
btn3.grid(column=1, row=0)
btn3['font'] = myFont

window.mainloop()   

exit