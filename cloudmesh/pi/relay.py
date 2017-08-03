import time
import grovepi
import sys



class Relay(object):

    def __init__(self, pin=4):
        """
        connect relay to digital port. D4 is default.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")

    def on(self):
        """
        Sets relay on. Allows current to flow.
        :return: None
        """
        try:
            grovepi.digitalWrite(self.pin, 1)
            print('on')
        except IOError:
            print('Error')

    def off(self):
        """
        sets relay off. Stops current flow.
        :return:
        """
        try:
            grovepi.digitalWrite(self.pin, 0)
            print('off')
        except IOError:
            print('Error')

    def put(self, value):
        """
        sets relay to given status. value=0 for off, value=1 for on
        :param value: Integer
        :return: None
        """
        try:
            grovepi.digitalWrite(self.pin, value)
            print(value)
        except IOError:
            print('Error')

    
if __name__=="__main__":

    r1 = Relay()
    r2 = Relay(pin=2)
    r1.on()
    r2.on()
    time.sleep(2.5)
    r1.off()
    r2.off()
    time.sleep(30)
    print('done')
