# read analog value on turbidity sensor
# display the reading on lcd screen
# display a level on the ledbar

# high reading means less turbidity ahd hence is good

from cloudmesh.pi import LedBar
from cloudmesh.pi import LCD
from cloudmesh.pi import TurbiditySensorAnalog
import time
#connect lcd to i2c port
#connect turbidity sensor to analog port A0
#connect ledbar to digital port D3

lcd = LCD()
lcd.setRGB(0,128,0)
ledbar = LedBar(pin=3)
turb = TurbiditySensorAnalog(pin=0)

while True:
	value = turb.getValue()
	level = value/100
	ledbar.setLevel(level)
	lcd.setText("Turbidity : " + str(value) )
	time.sleep(1)

