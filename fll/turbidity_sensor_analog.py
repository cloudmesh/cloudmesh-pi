from __future__ import print_function
from cloudmesh.pi import TurbiditySensorAnalog
import time

print("Starting ...")
turbidity = TurbiditySensorAnalog()
while True:
    value = turbidity.getValue()
    print("The turbidity value is ", value)
    time.sleep(1)
