import time
import grovepi

class WaterSensor(object):

    def __init__(self, pin=2):
        """
        connect sensor to digital port. D2 is default.
        :param pin: Number
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "INPUT")

    def get(self):
        """
        gets the value measured by water sensor.
        :return: Integer
        """
        return grovepi.digitalRead(self.pin)

if __name__ == "__main__":

    ws = WaterSensor()
    water = ws.get()
    print(water)
