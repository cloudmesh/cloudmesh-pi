import time
import grovepi

class Joystick(object):

    # My Joystick
    #     Min  Typ  Max  Click
    #  X  268  497  755  1020-1023
    #  Y  267  514  756

    # max y = 756
    # min y = 267
    # max x = 755
    # min x = 269

    def __init__(self):
        """
        Connect the Joystick to an analog port. A0 is the default.
        """
        self.xPin = 0
        self.yPin = 1
        grovepi.pinMode(self.xPin, "INPUT")
        grovepi.pinMode(self.yPin, "INPUT")
        self.max_y = 756
        self.min_y = 267
        self.max_x = 755
        self.min_x = 269
        self.typical_x = 498
        self.typical_y = 514

    def get(self):
        """
        gets the x, y, and click status of the joystick
        :return: Integer, Integer, Integer : x, y, click
        """
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(self.xPin)
            y = grovepi.analogRead(self.yPin)

            # Was a click detected on the X axis?
            click = 1 if x >= 1020 else 0

            print("x =", x, " y =", y, " click =", click)
            x = x - self.typical_x
            y = y - self.typical_y

            if abs(x) <= 1:
                x = 0
            if abs(y) <= 1:
                y = 0
            return x, y, click

        except IOError:
            print ("Error")
            x = 0
            y = 0

    def get_absolute(self):
        """
        gets the difference between the x, y, and click positions and their minimum values
        :return: Number, Number, Number : x, y, click
        """
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(self.xPin)
            y = grovepi.analogRead(self.yPin)

            # Was a click detected on the X axis?
            click = 1 if x >= 1020 else 0

            print("x =", x, " y =", y, " click =", click)
            return x - self.min_x, y - self.min_y, click

        except IOError:
            print ("Error")
            x = self.typical_x - self.min_x
            y = self.typical_y - self.min_y



if __name__ == "__main__": 
    stick = Joystick() 
    print(stick.get_absolute())
    print(stick.get())
