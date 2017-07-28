import time
import grovepi

class Button(object):

    def __init__(self, pin=3):
        self.pin = 3
        grovepi.pinMode(self.pin,"INPUT")

    def get(self):
        return grovepi.digitalRead(self.pin)

if __name__ == "__main__":

    button = Button(pin=3)
    
    while True:
        try:
            print(button.get())
            time.sleep(.5)
        except IOError:
            print ("Error")


