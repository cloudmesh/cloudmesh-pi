import time
from grovepi import *

print ("This example will blink a Grove LED connected to the GrovePi+ on the port labeled D3.\nIf you're having trouble seeing the LED blink, be sure to check the LED connection and the port number.\nYou may also try reversing the direction of the LED on the sensor.")
print (" ")
print ("Connect the LED to the port labele D3!" )


class LED(object):

    def __init__(self, pin):
        self.pin = pin
        pinMode(self.pin, "OUTPUT")

    def blink(self, n):
        for n in range(0, n):
            try:
                # Blink the LED
                digitalWrite(self.pin, 1)  # Send HIGH to switch on LED
                print ("LED ON!")
                time.sleep(1)

                digitalWrite(self.pin, 0)  # Send LOW to switch off LED
                print ("LED OFF!")
                time.sleep(1)

            except KeyboardInterrupt:  # Turn LED off before stopping
                digitalWrite(self.pin, 0)
                break
            except IOError:  # Print "Error" if communication error encountered
                print ("Error")

led = LED(3)
led.blink(5)
