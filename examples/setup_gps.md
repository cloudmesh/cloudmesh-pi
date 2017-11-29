## Instructions to get GPS working

* go to raspberry pi configuration and disable camera\
* reboot pi
* again, go to raspberry pi configuratin and enable uart
* reboot the pi
* again go to raspberry pi configuration and enable camera if needed
* reboot the pi
* connect th gps sensor to RPISER port on the grovepi

At this point running ls /dev/ttyS* should show the serial port /dev/ttyS0

Next we need to make sure other system programs do not use the serial port,
so that we dont have interference on the serial port

* run command cp /boot/cmdline/txt /boot/cmdline.back.txt
* the above command creates a backup of the configuration passed to the kernel at boot time
* run sudo nano /boot/cmdline.txt
* remove console=serial0, 115200, so that the line looke like the following
	dwc_otg.lpm_enable=0  root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait splash plymouth.ignore-serial-consoles

* disconnect the gps senspr and reboot the pi
* connect the gps sensor once the pi reboots
* now you should be able to read the sensor value via serial port /dev/ttyS0 using cloudmesh.pi GPS library

