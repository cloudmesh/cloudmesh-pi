
######################################################################
# This program reads analog turbidity sensor values and
# displays it on the terminal
#
# Connect the turbidity sensor to port A0 of the grovepi
# Connect LCD to an I2C port of grovepi
#
# Question: can we use any I2C and any analog port.
# Is there a combination the would not work
#
######################################################################
from __future__ import print_function
from cloudmesh.pi import TurbiditySensorAnalog
import time

turbidity = TurbiditySensorAnalog(pin=0)

while True:
    value = turbidity.getValue()
    print("Turbidity : " + str(value))
    time.sleep(1)
