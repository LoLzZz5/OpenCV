import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '...'

img = cv2.imread('...')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))

cv2.imshow('Img', img)
cv2.waitKey(0)