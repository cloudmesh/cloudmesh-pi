import time
import grovepi


class GroveUVSensor:
    def __init__(self, pin=0):
        """
		use analog pin A0  for the input by default
		connect to port A0 of grovepi hat
		"""
        self.uv_sensor = pin
        grovepi.pinMode(self.uv_sensor, "INPUT")

    def getUVIndex(self):
        """
		calculate an estimate value of the uv index as per grove seed website
		"""
        val = grovepi.analogRead(self.uv_sensor)
        illumination_intensity = val * 307
        uv_index = illumination_intensity / float(200)
        return uv_index


if __name__ == "__main__":
    uv_sensor = GroveUVSensor()

    while True:
        try:
            uv_index = uv_sensor.getUVIndex()
            print(uv_index)
            time.sleep(0.5)

        except IOError as e:
            print(e)
# test in day time somehow
# try mean method
