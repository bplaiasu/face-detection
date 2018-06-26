import cv2
import sys

# Get user supplied values
imagePath = "training-data/s2/6.jpg"
# cascPath = "xml/haarcascades/haarcascade_frontalface_default.xml"
cascPath = "xml/haarcascades/haarcascade_frontalface_alt2.xml"


# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#print(gray);

# Detect faces in the image
faces = faceCascade.detectMultiScale(
	gray,
    scaleFactor = 1.2,
	minNeighbors = 5,
	minSize = (20, 20)
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow("Faces found", image)
cv2.waitKey(0)