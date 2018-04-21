import grovepi
import time
import sys


class GroveSpeaker:
    def __init__(self, pin=3):
        """
        use digital pin as output pin for speaker
        pin 3 by default
        connect to port D3 of grove pi hat
        """
        self.speaker = 3
        self.high = 0
        self.low = 0
        grovepi.pinMode(self.speaker, "OUTPUT")
        grovepi.digitalWrite(self.speaker, self.low)

    def setFreq(self, freq=0, seconds=0.0):
        """
        Generate a wave with the frequency freq (Hz) for specified number of seconds approximately
        by default 0 Hz for 0 seconds

        for freq time for each wavelength = 1/freq
        time for half a wave = wait_time = 1/(2*freq)

        number of wavelengths in specified seconds = loop
        loop = seconds * freq
        """
        wait_time = 1 / (2 * float(freq))
        loop = int(seconds * freq)

        for i in range(loop):
            grovepi.digitalWrite(self.speaker, self.high)
            time.sleep(wait_time)
            grovepi.digitalWrite(self.speaker, self.low)
            time.sleep(wait_time)

    def setVolumeHigh(self):
        """
        When high = 1, low = 0 , more voltage to the speaker, therefore more volume
        """
        self.high = 1

    def setVolumeLow(self):
        """
        when high = 0 and low = 0, very little voltage goes to the speaker and therefore low  volume
        """
        self.high = 0

    def speakerOff(self):
        """
        to avoid some noise voltage to speaker leading to some noise in the speaker set voltage to -1
        """
        grovepi.digitalWrite(self.speaker, -1)

    def speakerOn(self):
        """
        to activate the speaker or allow some noise set voltage to 0
        """
        grovepi.digitalWrite(self.speaker, 0)


if __name__ == "__main__":
    speaker = GroveSpeaker()
    print("set speaker off to avoid noise")
    speaker.speakerOff()
    time.sleep(1)

    print("set speaker volume high")
    speaker.setVolumeHigh()

    print("play a certain tune 10 times")
    print("play a tone with frequency 200 for 0.05 seconds")
    print("play a tone with frequency 500  for 0.05 seconds")
    print("play a tone with frequency 1000  for 0.05 seconds")
    print("repeat")

    for i in range(10):
        speaker.setFreq(200, 0.03)
        speaker.setFreq(500, 0.03)
        speaker.setFreq(1000, 0.03)
    print("set speaker volume low")
    speaker.setVolumeLow()

    print("play the same tune for 10 times")
    for i in range(10):
        speaker.setFreq(200, 0.03)
        speaker.setFreq(500, 0.03)
        speaker.setFreq(1000, 0.03)

    print("turn speaker off")
    speaker.speakerOff()
