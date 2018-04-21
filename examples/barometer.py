from cloudmesh.pi import Barometer

if __name__ == "__main__":
    barometer = Barometer()
    print(barometer)
    print(barometer.get())
