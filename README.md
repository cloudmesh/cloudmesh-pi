# New:


    mkdir ~/github
    cd ~/github
    git clone https://github.com/cloudmesh/cloudmesh.pi.git
    cd cloudmesh.pi
    make install-driver

reboots

    make install-grovepi

reboot

.... do what you like



# Dev: Cloudmesh Raspberry PI Library 

    mkdir ~/github
    cd ~/github
    git clone https://github.com/cloudmesh/cloudmesh.pi.git
    pip install .

This code contains some Grove Sensor libraries for developping IoT
and Robot projects tith Raspberry Pi and GRovePI+.


* https://pinout.xyz/

GrovePI Pinout

* https://32414320wji53mwwch1u68ce-wpengine.netdna-ssl.com/wp-content/uploads/2013/07/grovepi_pinout.png

GroveZero Pinout

* https://32414320wji53mwwch1u68ce-wpengine.netdna-ssl.com/wp-content/uploads/2013/07/GrovePi-Zero-Pinout-diagram.png


* https://www.dexterindustries.com/GrovePi/engineering/port-description/

# Notes

# Enable remote access

enable vnc
enable ssh

# Install GrovePi

Do not install the Grovepi shield yet

   sudo apt-get update
   sudo apt-get install emacs -y
   cd /home/pi/Desktop
   sudo git clone https://github.com/DexterInd/GrovePi
   cd /home/pi/Desktop/GrovePi/Script
   sudo chmod +x install.sh
   sudo ./install.sh
   sudo reboot

Now we install grovepi

    sudo pip install grovepi
    sudo shutdown -h now
    
    
put the grove shield on and power on

check 

    sudo i2cdetect -y 1
    
If everything goes right you will see:
         
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- 04 -- -- -- -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --        
    
# Test a joystick

    cd ~/Desktop/GrovePi/Software/Python/   
    python grove_thumb_joystick.py
