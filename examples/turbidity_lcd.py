######################################################################
# This program reads analog turbidity sensor values and
# displays it on the lcd screen
#
# Connect the turbidity sensor to port A0 of the grovepi
# Connect LCD to an I2C port of grovepi
#
# Question: can we use any I2C and any analog port.
# Is there a combination the would not work
#
######################################################################

from cloudmesh.pi import LCD
from cloudmesh.pi import TurbiditySensorAnalog
import time

turb = TurbiditySensorAnalog(pin=0)
screen = LCD()
screen.setRGB(0,128,0)

while True:
	value = turb.getValue()
	screen.setText("Turbidity : " + str(value) )
	time.sleep(1)
