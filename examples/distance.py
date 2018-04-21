from cloudmesh.pi import DistanceSensor

if __name__ == "__main__":

    distance = DistanceSensor()

    while True:
        try:
            # Read distance value from Ultrasonic
            print(distance.get())

        except TypeError:
            print("Error")
        except IOError:
            print("Error")
