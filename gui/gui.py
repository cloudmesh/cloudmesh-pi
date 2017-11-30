from guizero import App, Text, Box, PushButton, Picture
import datetime
from time import gmtime, strftime
import os
font_size = 12

# create global variables.
now = "..."
temperature = "..."
turbidity = "..."
sun = "..."
chop = "..."
observer = "starboat"
gps = "..."
#wind

counter = 1

filename = os.path.expanduser("~/data.log")

def do_measure():

    global now, temperature, turbidity, sun, chop, observer, gps, counter
    
    counter = counter + 1
    now = datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')

    # get values from pi
    # update values to global vars (time, temperature)

    entry("Counter:", counter, 0,1)
    entry("Time:", now, 0,2)
    entry("Temperature:", temperature, 0, 3)
    entry("Turbidity:", turbidity, 0, 4)
    entry("Sun:", sun, 0, 5)
    entry("Chop:", chop, 0, 6)
    entry("GPS:", gps, 0, 7)
    entry("Observer:", observer, 0, 8)

    with open(filename, "a") as myfile:
        myfile.write(now + ", " + temperature + "\n")
    
    return 0

def entry(label, value, x, y):
    l = Text(app, text=label,  size=font_size, align="left",  grid=[y,x])
    t = Text(app, text=value, size=font_size, align="left", grid=[y, x+1])
    print (label, value)
    

app = App(title="Starboat Data", height=300, width=400, layout="grid")

# picture = Picture(app, image="logo.gif", grid=[0,0])

entry("Counter:", counter, 0,1)
entry("Time:", now, 0,2)
entry("Temperature:", temperature, 0, 3)
entry("Turbidity:", turbidity, 0, 4)
entry("Sun:", sun, 0, 5)
entry("Chop:", chop, 0, 6)
entry("GPS:", gps, 0, 7)
entry("Observer:", observer, 0, 8)

button = PushButton(app, command=do_measure, text="measure", grid=[0,0])
app.display()
