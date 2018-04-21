"""Usage: led.py [-h] pin=PIN
Demonstrate a blinking LED on given PIN
Arguments:
  PIN     The PIN number  [default: 3].
Options:
  -h --help
"""
from docopt import docopt

import time
import grovepi
import sys


class LED(object):
    def __init__(self, pin=3):
        """
        Connect the LED to a digital port. 3 is default.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")

    def on(self):
        """
        turns LED on.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 1)  # Send HIGH to switch on LED

    def off(self):
        """
        turns LED off.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 0)  # Send LOW to switch off LED

    def blink(self, n, t=0.2):
        """
        blinks LED n times with t time delay. Default t is .2 seconds.
        :param n: Integer
        :param t: Number
        :return: None
        """
        for i in range(0, n):
            try:
                # LED on
                self.on()
                time.sleep(t)  # duration on
                # LED off
                self.off()
                time.sleep(t)  # duration off

            except KeyboardInterrupt:  # Turn LED off before stopping
                grovepi.digitalWrite(self.pin, 0)
                sys.exit()
                # break
            except IOError:  # Print "Error" if communication error encountered
                print("Error")


if __name__ == "__main__":
    #    arguments = docopt(__doc__)
    #    pin = arguments['PIN']

    #    led = LED(pin=pin)
    led = LED(pin=3)
    led.blink(5)
