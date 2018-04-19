import os
import time
import datetime
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

    def __init__(self,calibrate=False):
        """
        Connect the Joystick to an analog port. A0 is the default.
        """
        self.config_file = "~/.cloudmesh/pi/joystick.ini"
        # file format of the config file:
        '''
        x:-1
        y:-1
        xmin:-1
        xmax:-1
        ymin:-1
        ymax:-1
        click:1000
        '''
        self.xPin = 0
        self.yPin = 1
        grovepi.pinMode(self.xPin, "INPUT")
        grovepi.pinMode(self.yPin, "INPUT")
        if calibrate:
            self.calibrate()
        self.config = self.read_calibrate()
        self.max_y = self.config["ymax"]
        self.min_y = self.config["ymin"]
        self.max_x = self.config["xmax"]
        self.min_x = self.config["xmin"]
        self.x0 = self.config["x0"]
        self.y0 = self.config["y0"]

    def calibrate(self):
        config = self.read_calibrate()
        print (config)
        ntries = 10
        #
        # check the still position for x0, y0
        #
        print ("...Calibrating... DO NOT touch the joystick...")
        time.sleep(2)
        xsum = 0
        ysum = 0
        for i in range(1,ntries+1):
            (x,y) = self.get_raw()
            xsum += x
            ysum += y
            time.sleep(0.2)
        config["x0"] = int(xsum/10)
        config["y0"] = int(ysum/10)
        time.sleep(3)
        #
        # check the left most position value
        # x_min
        #
        print ("...Move the joystick to the LEFT most position and hold...")
        time.sleep(2)
        xmin = 1024
        for i in range(1,ntries+1):
            (x,y) = self.get_raw()
            if x < xmin:
                xmin = x
            time.sleep(0.2)
        config["xmin"] = xmin
        time.sleep(3)
        print ("Release...")
        time.sleep(2)
        #
        # check the right most position value
        # x_max
        #
        print ("...Move the joystick to the RIGHT most position and hold...")
        time.sleep(2)
        xmax = -1
        for i in range(1,ntries+1):
            (x,y) = self.get_raw()
            if x > xmax:
                xmax = x
            time.sleep(0.2)
        config["xmax"] = xmax
        time.sleep(3)
        print ("Release...")
        time.sleep(2)
        #
        # check the down most position value
        # y_min
        #
        print ("...Move the joystick to the DOWN most position and hold...")
        time.sleep(2)
        ymin = 1024
        for i in range(1,ntries+1):
            (x,y) = self.get_raw()
            if y < ymin:
                ymin = y
            time.sleep(0.2)
        config["ymin"] = ymin
        time.sleep(3)
        print ("Release...")
        time.sleep(2)
        #
        # check the up most position value
        # y_max
        #
        print ("...Move the joystick to the UP most position and hold...")
        time.sleep(2)
        ymax = -1
        for i in range(1, ntries + 1):
            (x, y) = self.get_raw()
            if y > ymax:
                ymax = y
            time.sleep(0.2)
        config["ymax"] = ymax
        time.sleep(3)
        print ("Release...")
        time.sleep(2)
        with open(os.path.expanduser(self.config_file), "w") as fh:
            for k in config.keys():
                fh.write("%s:%s\n" % (k, config[k]))

    def read_calibrate(self):
        config = {}
        with open(os.path.expanduser(self.config_file)) as fh:
            fcontent = fh.read().strip()
            lines = fcontent.split("\n")
            for line in lines:
                k, v = line.split(":")
                config[k] = int(v)
        return config

    def get_raw(self):
        x = -1
        y = -1
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(self.xPin)
            y = grovepi.analogRead(self.yPin)
        except IOError:
            print ("IOError")
        return (x,y)

    # x,y values normalized in the range of [-100, 100]
    def get_scaled(self):
        (x,y,z) = self.get()
        if x > 0:
            x = x * 100/(self.max_x - self.x0)
        else:
            if x < 0:
                x = x * 100 / (self.x0 - self.min_x)
        if y > 0:
            y = y * 100/(self.max_y - self.y0)
        else:
            if y < 0:
                y = y  * 100 / (self.y0 - self.min_y)
        return (x,y,z)

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
            click = 1 if x >= self.config["click"] else 0

            #print("x =", x, " y =", y, " click =", click)
            x = x - self.x0
            y = y - self.y0

            if abs(x) <= 1:
                x = 0
            if abs(y) <= 1:
                y = 0

            # when click, x value no meaning at all so set to zero
            if click == 1:
                x = 0
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
            click = 1 if x >= self.config["click"] else 0

            print("x =", x, " y =", y, " click =", click)
            return x - self.min_x, y - self.min_y, click

        except IOError:
            print ("Error")
            x = self.x0 - self.min_x
            y = self.y0 - self.min_y



if __name__ == "__main__":
    # call with calibrate
    stick = Joystick(calibrate=True)
    #print(stick.get_absolute())
    print(stick.get_scaled())
    # assuming calibrate had been done
    stick = Joystick()
    #print(stick.get_absolute())
    print(stick.get_scaled())
