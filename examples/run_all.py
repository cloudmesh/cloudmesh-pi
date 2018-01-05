from cloudmesh.pi import *

temperature, humidity = TemperatureSensor(port=7)

turbidity = TurbiditySensorAnalog(pin=2)

air_quality = GroveAirQualitySensor(pin=0)

print "Temperature: " + str(temperature)
print "Humidity:" + str(humidity)
print "Turbidity:" + str(turbidity.getValue())
print "Air Quality:" + str(air_quality.get())