from cloudmesh.pi import LED

if __name__ == "__main__":
#    arguments = docopt(__doc__)
#    pin = arguments['PIN']

#    led = LED(pin=pin)
    led = LED(pin=3)
    led.blink(5)
