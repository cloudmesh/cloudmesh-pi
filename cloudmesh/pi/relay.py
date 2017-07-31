import time
import grovepi
import sys

class Relay(object):

    def __init__(self, pin=4):
        self.pin = pin
        grovepi.pinMode(self.pin,"OUTPUT")

    def on(self):
        try:
            grovepi.digitalWrite(self.pin, 1)
            print('on')
        except IOError:
            print('Error')

    def off(self):
        try:
            grovepi.digitalWrite(self.pin, 0)
            print('off')
        except IOError:
            print('Error')

    def put(self, value):
        try:
            grovepi.digitalWrite(self.pin, value)
            print(value)
        except IOError:
            print('Error')

class Dendrite(object):

    def __init__(self, pin=4):
        self.last = None
        self.pin = pin
        self.relay = Relay(pin=self.pin)

    def react_and_wait(self, on=2.5, relax=30):
        self.last = time.time()
        self.relay.on()
        time.sleep(on)
        self.relay.off()
        time.sleep(relax)

    def react(self, on=2.5, relax=30):
        if self.ready(relax):
            self.last = time.time()
            self.relay.on()
            time.sleep(on)
            self.relay.off()

    def ready(self, delta):
        t = time.time()
        return t - self.reacted >= delta

class DendriteSwarm(object):

    def __init__(self, pins=[4,4]):
        self.last = None
        self.pins = pins
        self.relays = []
        for pin in pins:
            self.relays.append(Relay(pin=self.pin))
            
    def dance(self, on=2.5, relax=30, delta[0,1]):
        self.last = time.time()

        i = 0
        for relay in self.releay
            time.sleep(delta[i])
            relay.on()
            i = i + 1

        time.sleep(on)

        i = 0
        for relay in self.releay
            time.sleep(delta[i])
            relay.off()
            i = i + 1            

    def react(self, on=2.5, relax=30):
        if self.ready(relax):
            self.last = time.time()

            for relay in self.releay
                relay.on()

            time.sleep(on)

            for relay in self.releay
                relay.off()

    def ready(self, delta):
        t = time.time()
        if self.last is None:
            return True
        return t - self.reacted >= delta


    
if __name__=="__main__":
#    t0 = datetime.now()
#    print(t0)
#    sys.exit()
    d1 = Dendrite(pin=4)
    d2 = Dendrite(pin=2)
    d1.react(on=2, relax=30)
    d2.react(on=2, relax=30)

# r1 = Relay()
   # r2 = Relay(pin=2)
   # r1.on()
   # r2.on()
   # time.sleep(2.5)
 #   r1.off()
 #   r2.off()
 #   time.sleep(30)
    print('done')
