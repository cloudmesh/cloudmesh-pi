import picamera
import time
import os


class Camera:
    def __init__(self):
        """
        initialize the camera
        """
        self.cam = picamera.PiCamera()
        self.cam.preview_window = (620, 320, 640, 480)

    def get(self, filename="image.jpg"):
        """
        get an image from the camera and save it to a file

        :param filename: the name to save the image in. default is image.jpg
        """
        self.cam.capture(filename)

    def view(self, filename="image.jpg"):
        """
        starts the camera preview to look at images saved in a file

        :param filename: the name to save the image in. default is image.jpg
        """
        command = "see " + filename
        os.system(command)


if __name__ == "__main__":
    cam = Camera()
    print("capture image")
    cam.get()

    print("display image")
    cam.view()
