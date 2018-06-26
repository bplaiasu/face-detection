import cv2
import pickle
import numpy as np

face_cascade = cv2.CascadeClassifier('xml/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('xml/haarcascades/haarcascade_eye.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {}
with open("label.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

# set the frame width and height
# 3 - width; 4 - height
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(frame, scale_percent=75):
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    # resize the frame - for a smoother image
    frame = rescale_frame(frame, scale_percent=75)

    # convert the image to gray colors
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        # roi - region of interest
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        id_, conf = recognizer.predict(roi_gray)
        # print(conf);
        if (100 - conf) >= 35 and (100 - conf) <= 85:
            font = cv2.FONT_HERSHEY_PLAIN
            name = labels[id_] + ' - ' + str(100.00 - round(conf, 2)) + '%'
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1.5, color, stroke, cv2.LINE_AA)
        #     print(id_)
        #     print(labels[id_])



        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)     # save only the face, not the entire image

        # draw a rectangle around faces
        color = (0, 255, 0)    # set the rectangle color
        stroke = 2
        end_x = x + w
        end_y = y + h
        cv2.rectangle(frame, (x, y), (end_x, end_y), color, stroke)

        # eyes= eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), stroke)

    # display the resulting frame
    window_name = "Video Frame ..."
    cv2.namedWindow(window_name)
    cv2.moveWindow(window_name, 200, 100)
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
