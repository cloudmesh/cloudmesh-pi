#!/usr/bin/env python

# 21cm = 26
# 31cm = 36
# 41cm = 49
# 51cm = 62
# 61cm = 75
# 71cm = 86
# 81cm = 99

# If value is smaller than 7 cm, take value.
import grovepi


class Distance(object):
    def __init__(self, port=4):
        # Connect the Grove Ultrasonic Ranger to digital port D4
        # SIG,NC,VCC,GND
        self.ultrasonic_ranger = port

    def get(self):
        return grovepi.ultrasonicRead(self.ultrasonic_ranger)


if __name__ == "__main__":

    distance = Distance()

    while True:
        try:
            # Read distance value from Ultrasonic
            print(distance.get())

        except TypeError:
            print("Error")
        except IOError:
            print("Error")
