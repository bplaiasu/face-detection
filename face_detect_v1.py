# import required libraries
import cv2
# importing time library for speed comparisons of both classifiers
import time
# import matplotlib library
import matplotlib.pyplot as plt


def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def detect_faces(f_cascade, colored_img, scaleFactor = 1.1):
    # just making a copy of image passed, so that passed image is not changed
    img_copy = colored_img.copy()

    # convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    # let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5)

    # go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return img_copy



#load test image
# test_image = cv2.imread('training-data/s3/4.jpg')
test_image = cv2.imread('test-data/20.jpg')


#load cascade classifier training file for haarcascade  - alt2 good
# haar_face_cascade = cv2.CascadeClassifier('xml/haarcascades/haarcascade_frontalface_default.xml')
haar_face_cascade = cv2.CascadeClassifier('xml/haarcascades/haarcascade_frontalface_alt2.xml')
lbp_face_cascade = cv2.CascadeClassifier('xml/lbpcascades/lbpcascade_frontalface.xml')

# call function to detect faces
# faces_detected_img = detect_faces(haar_face_cascade, test_image, scaleFactor=1.2)

# display the gray image using OpenCV
# cv2.imshow('Test Image', convertToRGB(faces_detected_img))



# TEST1
#------------HAAR-----------
# note time before detection
t1 = time.time()
# call our function to detect faces
haar_detected_img = detect_faces(haar_face_cascade, test_image, scaleFactor=1.2)
# note time after detection
t2 = time.time()
# calculate time difference
dt1 = t2 - t1
#print the time difference
print("Haar cascade time - {0}".format(dt1))
#------------LBP-----------
#note time before detection
t1 = time.time()
#call our function to detect faces
lbp_detected_img = detect_faces(lbp_face_cascade, test_image, scaleFactor=1.2)
#note time after detection
t2 = time.time()
#calculate time difference
dt2 = t2 - t1
#print the time difference
print("LBP cascade time - {0}".format(dt2))


#----------Let's do some fancy drawing-------------
#create a figure of 2 plots (one for Haar and one for LBP)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(17, 6))

#show Haar image
ax1.set_title('Haar Detection time: ' + str(round(dt1, 3)) + ' secs')
ax1.imshow(convertToRGB(haar_detected_img))

#show LBP image
ax2.set_title('LBP Detection time: ' + str(round(dt2, 3)) + ' secs')
ax2.imshow(convertToRGB(lbp_detected_img))

#show images
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()