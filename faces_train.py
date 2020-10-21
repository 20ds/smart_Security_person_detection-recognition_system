# turning immages to trainable data
import os
import pickle

import cv2
import numpy as np
from PIL import Image


def run():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # file path

    image_dir = os.path.join(BASE_DIR, "images")   # image path

    face_cascade = cv2.CascadeClassifier(
        'cascade/data/haarcascade_frontalface_alt2.xml')   # classifier for frontal phase

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                # label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
                # (root = os.path.dirname(path))
                label = os.path.basename(root).replace(" ", "-").lower()
                #print(label, path)

                if label in label_ids:
                    pass
                else:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]
                # print(label_ids)
                # y_labels.append(label)  # some no for labels
                # x_train.append(path)

                pil_image = Image.open(path).convert(
                    "L")  # gray_scale converted
                image_array = np.array(pil_image, "uint8")
                # print(image_array)
                faces = face_cascade.detectMultiScale(
                    image_array, scaleFactor=1.1, minNeighbors=5)

                for (x, y, w, h) in faces:
                    roi = image_array[y:y + h, x:x + w]
                    x_train.append(roi)
                    y_labels.append(id_)

    # print(y_labels)
    # print(x_train)

    with open("labels.pickle", "wb") as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainner.yml")

    """varify this image ,turns into a numpy array ,
    probably want it to be a Gray_scale immage

    """

    """
    replacing any space if we done any mistake in the name of dir as well
    as we want all the label in lower case .lower() is just the safe guard

    we will use Pickle to save Label Ids

    """


if __name__ == "__main__":
    run()
# how can we grab the name of the folder (label for the images ) from the directory
