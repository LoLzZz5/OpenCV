import cv2
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = '...'

img = cv2.imread('text.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img)

translator = Translator()
text = translator.translate(text, dest = 'ru')

print(text.text)

cv2.imshow('Img', img)
cv2.waitKey(0)