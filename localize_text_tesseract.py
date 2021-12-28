# import the necessary packages
from pytesseract import Output
import pytesseract
import argparse
import cv2
# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="NutritionData/BlackBeansNutritionLabel.jpg")
#ap.add_argument("-c", "--min-conf", type=int, default=0, help=50)
#args = vars(ap.parse_args())

path = "NutritionData/BlackBeansNutritionLabel.jpg"
min_conf = 50.0

# load the input image, convert it from BGR to RGB channel ordering,
# and use Tesseract to localize each area of text in the input image
#image = cv2.imread(args["image"])
image = cv2.imread(path)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)

# loop over each of the individual text localizations
for i in range(0, len(results["text"])):
	# extract the bounding box coordinates of the text region from
	# the current result
	x, y, w, h = results["left"][i], results["top"][i], results["width"][i], results["height"][i]
 
	# extract the OCR text itself along with the confidence of the
	# text localization
	text = results["text"][i]
	conf = float(results["conf"][i])
  
  # filter out weak confidence text localizations
	if conf > min_conf):
    
		# strip out non-ASCII text so we can draw the text on the image
		# using OpenCV, then draw a bounding box around the text along
		# with the text itself
		text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 200, 100), 2)
		cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)
      
# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
