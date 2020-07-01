
# Import OpenCV library
import cv2

# Load a cascade file for detecting faces
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Load image
image = cv2.imread("index.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
faces = faceCascade.detectMultiScale(gray, 1.1,3)

for(x,y, w, h) in faces:
	cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0),2)
	
cv2.imshow('ddd', image)

print("finish");
cv2.waitKey()

