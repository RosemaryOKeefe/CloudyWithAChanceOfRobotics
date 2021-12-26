import pytesseract
import cv2
img = cv2.imread('data/NotWorking.png')
gray = cv2.imread("data/NotWorking.png",0)
cv2.imwrite('data/NotWorking.png', gray)
blur = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imwrite('data/not_blur.png', gray)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite('data/not_thresh.png', thresh)
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
cv2.imwrite("data/index_kernal.png", kernal)
dilate = cv2.dilate(thresh, kernal, iterations=1)
cv2.imwrite("data/index_dilate.png", dilate)

cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
results  = []
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    if h > 300 and w > 60:
        cv2.rectangle(img, (x, y), (x+w, y+h), (36, 255, 12), 2)
        ocr_result = pytesseract.image_to_string(img)
        ocr_result = ocr_result.split("\n")
        for item in ocr_result:
            results.append(item)
cv2.imwrite("data/index_bbox_new.png", img)