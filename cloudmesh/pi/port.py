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

    def port(self, pin):
        for p in self.names:
            if pin in self.names[p]:
                print (p, self.sanmes[p])
                
    def view(self, kind=None):
        pi3 = "https://32414320wji53mwwch1u68ce-wpengine.netdna-ssl.com/wp-content/uploads/2013/07/grovepi_pinout.png"
        zero = "https://32414320wji53mwwch1u68ce-wpengine.netdna-ssl.com/wp-content/uploads/2013/07/GrovePi-Zero-Pinout-diagram.png"
        if kind is None:
            kind = pi3
        elif kind in ['zero']:
            kind = zero
        else:
            kine = pi3
        os.system("epiphany-browser " + kind)
        pass

