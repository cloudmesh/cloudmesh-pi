import time
import grovepi


class Button(object):
    def __init__(self, pin=3):
        """
        Connect button to a digital port. Default is 3.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(pin, "INPUT")

    def get(self):
        """
        gets the value of the button. 0 if not pressed, 1 if pressed.
        :return: Integer
        """
        return grovepi.digitalRead(self.pin)


if __name__ == "__main__":

    button = Button(pin=3)

    while True:
        try:
            print(button.get())
            time.sleep(.5)
        except IOError:
            print("Error")
