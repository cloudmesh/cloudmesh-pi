#!/usr/bin/env python

import time
import grovepi


# Connect the Grove Thumb Joystick to analog port A0


class Joystick(object):
    def __init__(self):
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
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(self.xPin)
            y = grovepi.analogRead(self.yPin)

            # Was a click detected on the X axis?
            click = 1 if x >= 1020 else 0

            x = x - self.typical_x
            y = y - self.typical_y

            if abs(x) <= 1:
                x = 0
            if abs(y) <= 1:
                y = 0
            return x, y, click

        except IOError:
            print("Error")
            x = self.typical_x
            y = self.typical_y

    def get_absolute(self):
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(self.xPin)
            y = grovepi.analogRead(self.yPin)

            # Was a click detected on the X axis?
            click = 1 if x >= 1020 else 0

            print("x =", x, " y =", y, " click =", click)
            return x - self.min_x, y - self.min_y, click

        except IOError:
            print("Error")
            x = self.typical_x - self.min_x
            y = self.typical_y - self.min_y


# My Joystick
#     Min  Typ  Max  Click
#  X  268  497  755  1020-1023
#  Y  267  514  756

# max y = 756
# min y = 267
# max x = 755
# min x = 269

stick = Joystick()
print(stick.get_absolute())
print(stick.get())
