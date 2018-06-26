import cv2

# Create the haar cascade
face_cascade = cv2.CascadeClassifier("xml/haarcascades/haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("xml/haarcasscades/haarcascade_eye.xml")

# create the capture
video_capture = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # convert capture to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()
