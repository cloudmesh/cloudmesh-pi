## Instructions to get GPS working

* Go to raspberry pi configuration and disable camera
* reboot pi
* Again, go to raspberry pi configuration and enable uart
* reboot the pi
* Again go to raspberry pi configuration and enable camera if needed
* Reboot the pi
* Connect th gps sensor to RPISER port on the grovepi

At this point running ls `/dev/ttyS*` should show the serial port

    /dev/ttyS0

Next we need to make sure other system programs do not use the serial
port, so that we do not have interference on the serial port

* Create a backup of the configuration passed to the kernel at boot time

      cp /boot/cmdline/txt /boot/cmdline.back.txt

* Edit the `cmdline.txt` file

      sudo nano /boot/cmdline.txt

  and remove

      console=serial0, 115200

  so that the line looks like the following

      dwc_otg.lpm_enable=0 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait splash plymouth.ignore-serial-consoles

* Disconnect the gps sensor and reboot the pi
* Connect the gps sensor once the pi reboots
* Now you should be able to read the sensor value via serial port

      /dev/ttyS0

  using cloudmesh.pi GPS library

