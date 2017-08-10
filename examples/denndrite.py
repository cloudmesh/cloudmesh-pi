from cloudmes.pi import Dendrite

if __name__ == "__main__":

    d1 = Dendrite(pin=4)
    d2 = Dendrite(pin=2)
    d1.react(on=2, relax=30)
    d2.react(on=2, relax=30)

    print('done')
