import time
import grovepi
import sys


class Buzzer(object):
    def __init__(self, pin=3):
        """
        Connect buzzer to a digital port. Default is 3.
        :param pin: Integer
        """
        self.pin = pin
        grovepi.pinMode(self.pin, "OUTPUT")

    def on(self):
        """
        Turns buzzer on.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 1)  # Send high to switch on buzzer

    def off(self):
        """
        Turns the buzzer off.
        :return: None
        """
        grovepi.digitalWrite(self.pin, 0)  # Send low to switch off buzzer

    def beep(self, n, t=0.2):
        """
        Cycles the buzzer on and off n times with a t second delay. .2 seconds is the default delay.
        :param n: Integer
        :param t: Number
        :return: None
        """
        for i in range(0, n):
            try:
                # on
                self.on()
                time.sleep(t)  # duration on
                # off
                self.off()
                time.sleep(t)  # duration off

            except KeyboardInterrupt:  # Turn BUZZER off before stopping
                grovepi.digitalWrite(self.pin, 0)
                sys.exit()
                break
            except IOError:  # Print "Error" if communication error encountered
                print("Error")


if __name__ == "__main__":
    buzzer = Buzzer(pin=3)
    buzzer.beep(5)
