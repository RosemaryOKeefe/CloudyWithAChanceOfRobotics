import cv2
import pytesseract
img = cv2.imread("NutritionData/BlackBeansNutritionLabel.jpg")
img = cv2.resize(img, (300,600))
hImg, wImg, _ = img.shape

text = pytesseract.image_to_int(img, lang='eng')
list_of_words = text.split()
next_word = list_of_words[list_of_words.index('Protein') + 1]
print(next_word)

cv2.waitKey(0)