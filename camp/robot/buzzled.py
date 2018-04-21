import time
from grovepi import *
import grovepi

print("""This example will blink a Grove LED connected to the GrovePi+ 
on the "port labeled D3.\nIf you're having trouble seeing the 
LED blink, be sure to check the LED connection and the port number.
You may also try reversing the direction of the LED on the sensor.
""")
print()
print("Connect the LED to the port label D3!")


class LED(object):
    def __init__(self, pin):
        self.pin = pin
        pinMode(self.pin, "OUTPUT")

    def blink(self, n, t):
        for i in range(0, n):
            try:
                # Blink the LED
                digitalWrite(self.pin, 1)  # Send HIGH to switch on LED
                # print ("LED ON!")
                time.sleep(t)

                digitalWrite(self.pin, 0)  # Send LOW to switch off LED
                # print ("LED OFF!")
                time.sleep(t)

            except KeyboardInterrupt:  # Turn LED off before stopping
                digitalWrite(self.pin, 0)
                break
            except IOError:  # Print "Error" if communication error encountered
                print("Error")


led = LED(3)
t = 0.02
d = 0.01
while t >= d:
    print(t)
    led.blink(100, t)
    t = t - d


# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8

grovepi.pinMode(buzzer, "OUTPUT")

while True:
    try:
        # Buzz for 1 second
        grovepi.digitalWrite(buzzer, 1)
        print('start')
        time.sleep(1)

        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(buzzer, 0)
        print('stop')
        time.sleep(1)

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer, 0)
        break
    except IOError:
        print("Error")
