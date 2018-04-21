import grovepi
import time


class TurbiditySensorAnalog:
    def __init__(self, pin=0):
        """
		Initialise the sensor.
		read analog mode value of the turbidity sensor
		connect the turbidity sensor to port A0 of the grovepi
		"""
        self.turbidity_sensor = pin
        grovepi.pinMode(self.turbidity_sensor, "INPUT")

    def getValue(self):
        """
		read the value of the turbidity sensor in analog mode
		"""
        value = grovepi.analogRead(self.turbidity_sensor)
        return value


class TurbiditySensorDigital:
    def __init__(self, pin=4):
        """
		Initialise the sensor
		read digital mode value of the turbidity sensor
		connect the turbidity sensor to port D4 of the grovepi
		"""
        self.turbidity_sensor = pin
        grovepi.pinMode(self.turbidity_sensor, "INPUT")

    def getValue(self):
        """
		read the value of the turbidity sensor in digital mode
		"""
        value = grovepi.digitalRead(self.turbidity_sensor)
        return value


if __name__ == "__main__":
    turbidity = TurbiditySensorAnalog(pin=0)
    while True:
        value = turbidity.getValue()
        print(" Turbidity value is ", value)
        time.sleep(1)
