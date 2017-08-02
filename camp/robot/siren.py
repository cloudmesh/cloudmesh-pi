import grovepi

class Siren (object):
    def __init__(self,led,buzzer):
        self.led=led
        self.buzzer=buzzer
        grovepi.pinMode(buzzer, "OUTPUT")
        grovepi.pinMode(led, "OUTPUT")
        
    def start(self):
        grovepi.digitalWrite(self.led, 1)
        grovepi.digitalWrite(self.buzzer, 1)

    def stop(self):
        grovepi.digitalWrite(self.led, 0)
        grovepi.digitalWrite(self.buzzer, 0)
        
