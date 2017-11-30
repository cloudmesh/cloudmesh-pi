from guizero import App, Text, Box, PushButton
import datetime
from time import gmtime, strftime
import os
font_size = 12

# create global variables.
now = "measure"
temperature = "measure"

filename = os.path.expanduser("~/data.log")

def do_measure():
    global now, temperature
    # get values from pi
    # update values to global vars (time, temperature)
    now = datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    
    entry("Time:", now, 0,1)
    print ("Time", now)

    with open(filename, "a") as myfile:
        myfile.write(now + ", " + temperature + "\n")

    
    return 0

def entry(label, value, x, y):
    l = Text(app, text=label,  size=font_size, align="left",  grid=[y,x])
    t = Text(app, text=value, size=font_size, align="left", grid=[y, x+1])
    

app = App(title="My Application", height=300, width=400, layout="grid")

t = "0"
entry("Time:", now, 0,1)
entry("Temperature:", "temp", 0, 2)

button = PushButton(app, command=do_measure, text="measure", grid=[0,0])
app.display()
