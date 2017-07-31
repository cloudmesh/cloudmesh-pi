import time
import grovepi

# Connect the Grove Water Sensor to digital port D2
# SIG,NC,VCC,GND
class WaterSensor(object):

    def __init__(self, pin=2):
        """
        connect sensor to digital port
        :param pin: Number
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "INPUT")

    def get(self):
        return grovepi.digitalRead(self.pin)
