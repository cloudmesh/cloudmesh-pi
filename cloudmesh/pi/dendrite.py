class Dendrite(object):
    def __init__(self, pin=4):
        """
        connect to digital pin. default is D4.
        :param pin: Integer
        """
        self.last = None
        self.pin = pin
        self.relay = Relay(pin=self.pin)

    def react_and_wait(self, on=2.5, relax=30):
        """
        causes dendrite to react. current flows for 'on' seconds and relaxes for 'off' seconds.
        :param on: Number
        :param relax: Number
        :return: None
        """
        self.last = time.time()
        self.relay.on()
        time.sleep(on)
        self.relay.off()
        time.sleep(relax)

    def react(self, on=2.5, relax=30):
        """
        causes dendrite to react. current flows for 'on' seconds and relaxes for 'off' seconds.
        Will only react if ready.
        :param on: Number
        :param relax: Number
        :return: None
        """
        if self.ready(relax):
            self.last = time.time()
            self.relay.on()
            time.sleep(on)
            self.relay.off()

    def ready(self, delta=30):
        """
        returns True if dendrite has relaxed for 'delta' seconds. False otherwise. 30 seconds default.
        :param delta: Number
        :return: Boolean
        """
        t = time.time()
        return t - self.last >= delta


class DendriteSwarm(object):
    def __init__(self, pins=[4, 4]):
        """
        dendrite swarm connected to digital ports. D4 and D4 are the defaults.
        :param pins: ListOfIntegers
        """
        self.last = None
        self.pins = pins
        self.relays = []
        for pin in pins:
            self.relays.append(Relay(pin=pin))

    def dance(self, on=2.5, relax=30, delta=[0, 1]):
        """
        causes dendrites to activate for 'on' seconds. all relax for 'relax' seconds.
        stagger reactions by 'delta' seconds.
        :param on: Number
        :param relax: Number
        :param delta: ListOfNumbers
        :return:
        """

        self.last = time.time()

        i = 0
        for relay in self.relays:
            time.sleep(delta[i])
            relay.on()
            i = i + 1

        time.sleep(on)

        i = 0
        for relay in self.relays:
            time.sleep(delta[i])
            relay.off()
            i = i + 1

    def react(self, on=2.5, relax=30):
        """
        All dendrites react. On for 'on' seconds. Relax for 'relax' seconds.
        :param on: Integer
        :param relax: Integer
        :return: None
        """
        if self.ready(relax):
            self.last = time.time()

            for relay in self.relays:
                relay.on()

            time.sleep(on)

            for relay in self.relays:
                relay.off()

    def ready(self, delta):
        """
        returns whether or not the dendrite has relaxed for long enough
        :param delta: Number
        :return: Boolean
        """
        t = time.time()
        if self.last is None:
            return True
        else:
            return t - self.last >= delta


if __name__ == "__main__":
    d1 = Dendrite(pin=4)
    d2 = Dendrite(pin=2)
    d1.react(on=2, relax=30)
    d2.react(on=2, relax=30)

    print('done')

    # TODO add Dendrite swarm example
