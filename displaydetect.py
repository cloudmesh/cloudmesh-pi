'''
Create a copy of config.txt and rename it to config.txt.in

Add these lines to the end:
# customized display setting
hdmi_group=2
hdmi_mode=87
hdmi_cvt {x} {y} 60 6 0 0 0
display_rotate={display_rotate}

Add this to end of /etc/rc.local before the "exit 0" line:
/usr/bin/python /bin/displaydetect.py
'''

#!/usr/bin/python

import os, sys
import subprocess

displayconfig = "/boot/config.txt"

spec_old = subprocess.check_output(["egrep", "hdmi_cvt", displayconfig]).strip()

edidwritecmd = "/usr/bin/tvservice -d /boot/edid.dat > /dev/null 2>&1"
edidparsecmd = "/usr/bin/edidparser /boot/edid.dat > /boot/edid.txt"
os.system(edidwritecmd)
os.system(edidparsecmd)
displayconfigin = "/boot/config.txt.in"
f_edidspec = "/boot/edid.txt"

edidspec = ""
with open(f_edidspec) as fh:
    edidspec = fh.read()

reboot = False
template = ""
content = ""
with open(displayconfigin) as fh:
    template = fh.read()
if "1920" in edidspec:#!/usr/bin/python

import os, sys
import subprocess

displayconfig = "/boot/config.txt"

spec_old = subprocess.check_output(["egrep", "hdmi_cvt", displayconfig]).strip()

edidwritecmd = "/usr/bin/tvservice -d /boot/edid.dat > /dev/null 2>&1"
edidparsecmd = "/usr/bin/edidparser /boot/edid.dat > /boot/edid.txt"
os.system(edidwritecmd)
os.system(edidparsecmd)
displayconfigin = "/boot/config.txt.in"
f_edidspec = "/boot/edid.txt"

edidspec = ""
with open(f_edidspec) as fh:
    edidspec = fh.read()

reboot = False
template = ""
content = ""
with open(displayconfigin) as fh:
    tem/usr/bin/python /bin/displaydetect.pyplate = fh.read()
if "1920" in edidspec:
    content=template.format(x=1920,y=1080,display_rotate=0)
    reboot = "1920" not in spec_old
elif "1024" in edidspec:
    content=template.format(x=1024,y=600,display_rotate=0)
    reboot = "1024" not in spec_old
elif "800" in edidspec:
    template=template.format(x=480,y=800,display_rotate=3)
    reboot = "800" not in spec_old
else:
    pass

#print (content)
#print (spec_old)
#print (reboot)

if reboot:
    with open("/boot/config.txt", "w") as fh:
        fh.write(content)
    os.system("reboot")

    content=template.format(x=1920,y=1080,display_rotate=0)
    reboot = "1920" not in spec_old
elif "1024" in edidspec:
    content=template.format(x=1024,y=600,display_rotate=0)
    reboot = "1024" not in spec_old
elif "800" in edidspec:
    template=template.format(x=480,y=800,display_rotate=3)
    reboot = "800" not in spec_old
else:
    pass

#print (content)
#print (spec_old)
#print (reboot)

if reboot:
    with open("/boot/config.txt", "w") as fh:
        fh.write(content)
    os.system("reboot")
