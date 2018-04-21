import time
import grovepi


class LedBar(object):
    def __init__(self, pin=3, color=0):
        """
	    color = 0 starts counting led 1 from  the Red LED end
	    color = 0 starts counting led 1 from the green LED end
	    """

        self.ledbar = pin
        grovepi.ledBar_init(self.ledbar, color)


def setLevel(self, level=0):
    """
	level = 1-10
	level - 5 turns on LEDs 1 to 5
	"""


grovepi.ledBar_setLevel(self.ledbar, level)


def setLED(self, led=1, status=0):
    """
	led= number of led to set: 1- 10
	status 1= on, 0 = off
	"""


grovepi.ledBar_setLed(self.ledbar, led, status)


def toggleLED(self, led=0):
    """
	Inverts the status of the led
	"""


grovepi.ledBar_toggleLed(self.ledbar, led)

if __name__ == '__main__':
    ledbar = LedBar()
    ledbar.setLevel(5)
    time.sleep(0.2)
    ledbar.setLED(9, 1)
    while True:
        ledbar.toggleLED(2)
        time.sleep(0.2)
