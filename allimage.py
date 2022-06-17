import sys
import os
import cv2
import cv2
import time


import tkinter as tk
import tkinter.font as tkFont
#import Tkfont
from tkinter import *


#from Tkinter import font
#DATE=$(date +"%Y-%m-%d_%H%M")
#imagename -r 1280x720 --no-banner /home/pi/webcam/$DATE.jpg
imagename = "data/image.jpg"


def run():
    os.system('python nutrition_extract.py')
    
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

# program to capture single image from webcam in python
# importing OpenCV library
from cv2 import *
#import cv2.cv as cv

root = Tk()

w = Canvas(root, width=640, height=480, bd = 10, bg = 'white')
w.grid(row = 0, column = 0, columnspan = 2)

b = Button(width = 15, height = 2, text = 'Button1')
b.grid(row = 1, column = 0)
b2 = Button(width = 15, height = 2, text = 'Button2')
b2.grid(row = 1,column = 1)

cv2.namedWindow("camera",1)
capture = cv2.cv.CaptureFromCAM(0)
#capture = cv2.VideoCapture(0)

while True:
    img = cv2.QueryFrame(capture)
    img = cv2.query
    Canvas.create_image(0,0, image=img)
    if cv2.WaitKey(10) == 27:
        break

root.mainloop()



exit


# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
def cam_rec():
    cam_port = 0
    cam = VideoCapture(cam_port)
  
    # reading the input using the camera
    result, image = cam.read()
  
    # If image will detected without any error, 
    # show result`
    if result:
    
        # showing result, it take frame name and image 
        # output
        #imshow("GeeksForGeeks", image)
        img_name = 'data/cameracapture.jpg'
        # saving image in local storage
        imwrite(img_name, image)
    
        # If keyboard interrupt occurs, destroy image 
        # window
        imshow(img_name, image)
        waitKey(0)
        destroyWindow(img_name)
    
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
    return(img_name)





def webcapture():
    #key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    cv2.imshow("Capturing", frame)
    return()

def capture_img():
    check, frame = webcam.read()
    print(check) #prints true as long as the webcam is running
    print(frame) #prints matrix values of each framecd 
    cv2.imshow("Capturing", frame)
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    webcam.release()
    cv2.waitKey(1650)
    cv2.destroyAllWindows()   
    return()
