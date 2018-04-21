import grovepi
import time


class GroveRelay:
    def __init__(self, pin=3):
        """
        set the pin for relay
        by default pin 3
        """
        self.relay = pin
        grovepi.pinMode(self.relay, "OUTPUT")
        return

    def on(self):
        """
        turn on the relay allowing the current to flow through the connected device
        """
        grovepi.digitalWrite(self.relay, 1)
        return

    def off(self):
        """
        turn off the relay preventing current from flowing to the connected device
        """
        grovepi.digitalWrite(self.relay, 0)
        return


if __name__ == "__main__":
    relay = GroveRelay(4)
    relay.on()
    time.sleep(5)
    relay.off()
