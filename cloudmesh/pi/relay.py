import time
import grovepi
from datetime import datetime
import sys

class Relay(object):

    def __init__(self, port=4):
        self.port = port
        grovepi.pinMode(self.port,"OUTPUT")

    def on(self):
        try:
            grovepi.digitalWrite(self.port, 1)
            print('on')
        except IOError:
            print('Error')

    def off(self):
        try:
            grovepi.digitalWrite(self.port, 0)
            print('off')
        except IOError:
            print('Error')

    def put(self, value):
        try:
            grovepi.digitalWrite(self.port, value)
            print(value)
        except IOError:
            print('Error')

class Dendrite(object):

    def __init__(self, port=4):
        self.port = port
        self.relay = Relay(port=self.port)
        
    def react(self, on=2.5, relax=30):
        self.relay.on()
        time.sleep(on)
        self.relay.off()
        time.sleep(relax)

if __name__=="__main__":
#    t0 = datetime.now()
#    print(t0)
#    sys.exit()
    d1 = Dendrite(port=4)
    d2 = Dendrite)port=2)
    d.react(on=2, relax=30)
   # r1 = Relay()
   # r2 = Relay(port=2)
   # r1.on()
   # r2.on()
   # time.sleep(2.5)
 #   r1.off()
 #   r2.off()
 #   time.sleep(30)
    print('done')
