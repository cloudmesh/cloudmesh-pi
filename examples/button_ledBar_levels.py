######################################################################
# Connect a grove button to port D6 of grovepi
# Connect a grove led bar to port D3 of grovepi
# Run the program
# When you press the button, the level on the led bar increases until
# it is full, then it starts again
######################################################################

from cloudmesh.pi import Button
from cloudmesh.pi import LedBar
import time

b = Button(pin=6)
led_bar = LedBar()

test = 0

while True:
    test += b.get()
    print test
    value = test % 11
    print value
    led_bar.setLevel(value)
    time.sleep(0.2)
