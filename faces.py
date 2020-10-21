# OpenCv how to capture vedio / accessing the cam

import pickle

import cv2
import numpy as np


def run():

    face_cascade = cv2.CascadeClassifier(
        'cascade/data/haarcascade_frontalface_alt2.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")

    labels = {"person_name": 1}
    with open("labels.pickle", "rb") as f:

        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while True:
        # capture frame-by-frame
        ret, frame = cap.read()
        # we can make the fram gray scale
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray_scale, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            print(x, y, w, h)
            # (ycord_start, ycord_end)
            roi_gray = gray_scale[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Now we have Region of interest(roi)
            # How can we recognize the roi ?
            # OpenCv has the ability to train a recognizers
            # but this is where we could use a deep learned model to predict
            # things here as well by using keras/tensorflow/pytorch

            id_, conf = recognizer.predict(roi_gray)
            if conf >= 40:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_] + " ,confidance : " + str(conf)
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1,
                            color, stroke, cv2.LINE_AA)

            img_item = "my-image.png"
            cv2.imwrite(img_item, roi_gray)

            # Drawing the rectangle around the face
            color = (255, 0, 0)  # its in BGR
            stroke = 2
            end_cord_x = x + w    # end_cord_x or width
            end_cord_y = y + h   # end_cord_y or height
            cv2.rectangle(frame, (x, y), (end_cord_x,
                                          end_cord_y), color, stroke)

        cv2.imshow('frame', frame)   # to image show
        # user can exit the frame by pressing e on keyboard
        if cv2.waitKey(20) & 0xFF == ord("e"):
            break

    # When everything done ,release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
