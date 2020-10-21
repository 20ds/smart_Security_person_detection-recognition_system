import os
import time

import cv2


class CFEVideoConf(object):
    # Standard Video Dimensions Sizes
    STD_DIMENSIONS = {
        "360p": (480, 360),
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    # Video Encoding, might require additional installs
    VIDEO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    width = 640
    height = 480
    dims = (640, 480)
    capture = None
    video_type = None

    def __init__(self, capture, filepath, res="480p", *args, **kwargs):
        self.capture = capture
        self.filepath = filepath
        self.width, self.height = self.get_dims(res=res)
        self.video_type = self.get_video_type()

    # Set resolution for the video capture
    def change_res(self, width, height):
        self.capture.set(3, width)
        self.capture.set(4, height)

    def get_dims(self, res='480p'):
        width, height = self.STD_DIMENSIONS['480p']
        if res in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[res]
        self.change_res(width, height)
        self.dims = (width, height)
        return width, height

    def get_video_type(self):
        filename, ext = os.path.splitext(self.filepath)
        if ext in self.VIDEO_TYPE:
            return self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']


# adding new user (input will be taken by the webcam to register new user )
def register_user(user_name):
                               # user name would be taken as label , user can click images by pressing q key on keybord 10 times
                               # or images would be captured by default with a lapse of .5 sec
                               # 10 immages has been taken as of for this model to train on (accuracy will be less bcz of this )

    img_count = 10
    while(img_count > 0):
        cap = cv2.VideoCapture(0)
        save_path = r'C:\Users\Dharm\Documents\ComputerVission\face_recognition\vid.avi'
        frames_per_seconds = 24
        config = CFEVideoConf(cap, filepath=save_path, res='720p')
        out = cv2.VideoWriter(save_path, config.video_type,
                              frames_per_seconds, config.dims)

        # Capture frame-by-frame
        ret, frame = cap.read()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        path = r"C:\Users\Dharm\Documents\ComputerVission\face_recognition\images\{0}".format(
            user_name)

        if not os.path.exists(path):
            os.makedirs(path)
        cv2.imwrite(os.path.join(path, 'img_'
                                 + str(img_count) + '.jpg'), frame)
        img_count -= 1
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def run():  # user would be asked to enter his/her name as input
    # by pressing (q) on keyboard images would be captured (10 times needed form diff angles)
    usr_name = input("enter user name, and enter q to caputre : ")

    register_user(usr_name)


if __name__ == "__main__":
    usr_name = input("enter user name, and enter q to caputre : ")
    register_user(usr_name)
