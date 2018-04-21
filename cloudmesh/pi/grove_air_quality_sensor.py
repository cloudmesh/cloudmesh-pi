import time
import grovepi


class GroveAirQualitySensor:
    def __init__(self, pin=0):
        """
        Measuring Air Quality

        :param pin: The pin to use. pin A0 by default
        """
        self.air_sensor = pin
        grovepi.pinMode(self.air_sensor, "INPUT")

    def get(self):
        """
        returns the air quality value

        :return: the analog value of air quality received.
		         a smaller value means fresher air
        """
        value = grovepi.analogRead(self.air_sensor)
        return value


if __name__ == "__main__":
    air_quality_sensor = GroveAirQualitySensor()
    while True:
        value = air_quality_sensor.get()
        print("sensor value = ", value)
        time.sleep(0.5)
