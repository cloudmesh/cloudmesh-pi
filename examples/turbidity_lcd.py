#program reads analog turbidity sensor value
#displays it on the lcd screen

from cloudmesh.pi import LCD
from cloudmesh.pi import TurbiditySensorAnalog
import time
#connect turbidity sensor to port A0 of grovepi
# connect LCD to I2C port of grovepi

turb = TurbiditySensorAnalog(pin=0)
screen = LCD()
screen.setRGB(0,128,0)

while True:
	value = turb.getValue()
	screen.setText("Turbidity : " + str(value) )
	time.sleep(1)
