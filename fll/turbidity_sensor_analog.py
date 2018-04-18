from cloudmesh.pi import TurbiditySensorAnalog
import time
print "hola"
turb = TurbiditySensorAnalog()
while True:
	value = turb.getValue()
	print "The turbidity value is ", value
	time.sleep(1)
