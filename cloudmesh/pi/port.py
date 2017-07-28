class Port(object):

    def __init__(self):
        self.names = {
          "D7": [7,8],
          "D8": [8,9],
          "D5": [5,6],
          "D6": [6,7],
          "D4": [4,5],
          "D3": [4,3],
          "D2": [2,3]
        }

    def __str__(self):
        print(self.names)

    def pins (self, name):
        return self.names[name]

