import cv2
cam = cv2.videocapture(0)
cv2.namedWindow('Python Webcam')
img_counter=0

while True:
    ret,frame = cam.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('Test',frame)
    k=cv2.waitKey(1)
    if cv2.waitKey(1) & 0xff==ord('q'):
        print('Stopping app!')
        break
    elif k%256==32:
        img_name='frame.png'.format(img_counter)
        cv2.imwrite(img_name,frame)
        print('screenshot taken')
        img_counter+=1


cam.release()
cam.destroyAllWindows()


while True:
    import pytesseract as tess
    from PIL import Image
    img=Image.open('frame.png')
    text=tess.image_to_string(img)
    print(text)