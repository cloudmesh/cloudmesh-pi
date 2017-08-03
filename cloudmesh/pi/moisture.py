# 	Sensor values observer:
# 		Val  Condition
# 		0    sensor in open air
# 		18   sensor in dry soil
# 		425  sensor in humid soil
# 		690  sensor in water

import time
import grovepi

# Connect the Grove Moisture Sensor to analog port A0
# SIG,NC,VCC,GND


class MoistureSensor(object):

    def __init__(self, pin=0):
        """
        Connect sensor to analog port. A0 is default.
        :param pin: Number
        """
        self.pin = pin

    def get(self):
        return grovepi.analogRead(self.pin)

if __name__ == "__main__":

    ms = MoistureSensor()
    moisture = ms.get()
    print(moisture)
