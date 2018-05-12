# Tips

## Screenshots

To be able to do screenshots install

    sudo apt-get install scrot

To do a screenshot use

    scrot

# Internet connection SHaring

YOu can share teh internet with your computer, by enabeling it on your computer and than connecting to it from your PI. Follow the link for your OS:

* Mac OS: <https://support.apple.com/kb/PH6589>
* Windows <http://windows.microsoft.com/en-US/windows-vista/Using-ICS-Internet-Connection-Sharing>
* Ubuntu <https://help.ubuntu.com/community/Internet/ConnectionSharing>

# Web Server

A web server can be created with

    python -m SimpleHTTPServer

Files in the current working directory are accessible through the Pi’s IP address.

# TODO: raspberry PI local

Once you install 

    sudo apt-get install avahi-daemon

Now you can use `raspberrypi.local` as hostanme 

In

    /etc/avahi/avahi-daemon.conf

we set

    host-name= 

host-name= 


TODO: /etc/avahi/hosts: additional static hostname mappings to publish in mDNS, see avahi.hosts(5) for more information.

# Resoursces

* <https://makezine.com/2012/12/25/ten-raspberry-pi-tips/>
