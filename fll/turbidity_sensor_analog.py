from __future__ import print_function
from cloudmesh.pi import TurbiditySensorAnalog
import time

print("Starting ...")
turb = TurbiditySensorAnalog()
while True:
    value = turb.getValue()
    print("The turbidity value is ", value)
    time.sleep(1)
