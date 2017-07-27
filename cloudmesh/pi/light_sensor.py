import time
import grovepi


class LightSensor(object):

    def __init__(self, pin=0):
        self.pin = pin
        grovepi.pinMode(self.pin,"INPUT")

    def get(self):
        try:
            return grovepi.analogRead(self.pin)
        except IOError:
            print("Error")

l = LightSensor()
value = l.get()
print(value)
