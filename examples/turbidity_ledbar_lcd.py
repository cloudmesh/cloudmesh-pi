######################################################################
# Read the analog value on turbidity sensor
# Display the reading on lcd screen
# Display a level on the led bar
#
# High reading means less turbidity and hence is good
#
# Connect lcd to i2c port
# Connect turbidity sensor to analog port A0
# Connect led bar to digital port D3
#
######################################################################

from cloudmesh.pi import LedBar
from cloudmesh.pi import LCD
from cloudmesh.pi import TurbiditySensorAnalog
import time

lcd = LCD()
lcd.setRGB(0, 128, 0)
ledbar = LedBar(pin=3)
turbidity = TurbiditySensorAnalog(pin=0)

while True:
    value = turbidity.getValue()
    level = value / 100
    ledbar.setLevel(level)
    lcd.setText("Turbidity : " + str(value))
    time.sleep(1)
