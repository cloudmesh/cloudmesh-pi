import time
import grovepi


class LightSensor(object):
    def __init__(self, pin=0):
        """
        connect to analog port. A0 is default
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "INPUT")

    def get(self):
        """
        returns the sensor value
        :return: Integer
        """
        try:
            return grovepi.analogRead(self.pin)
        except IOError:
            print("Error")


if __name__ == "__main__":
    l = LightSensor()
    value = l.get()
    print(value)
