Steelseries Nimbus Bluetooth controller
=======================================
The Steelseries Nimbus Bluetooth gamecontroller works well with IOS, IpadOS, and TVOS devices but can be used in combination with the Raspberry Pi's Bullseye operationg system (and probably other versions)

How to connect the controller
-----------------------------

1. Check the content of the /dev/input folder before you connect the controller. 
Every connected input device like mice, keyboards and gamecontrollers is shown here. 
2. Connect and pair the bluetooth controller with the Raspberry Pi.
3. Check the content of the /dev/input folder again after the bluetooth controller is connected. 
2 new files are added now: eventX a and jsX. In this project, we need the "eventX" file. 
The number X can be different when other devices are added/removed before the controller. 
In order to use the controller in Python, a static device name can be handy.
 This can be done with so called udev rules. First, identify this specific controller:


udevadm info --attribute-walk /dev/input/event6|less

You can use multiple things to identify this specific controller but I used the name and the physical address. 

I created an udev rule:

/etc/udev/rules.d/98-controller.rules
and added the following content:

ATTRS{name}=="Nimbus", ATTRS{phys}=="e4:5f:01:0b:a3:ad", SYMLINK+="nimbus"


Restart your Pi or run the following command to enable the udev rule:

udevadm control --reload-rules && udevadm trigger

Reconnect the Controller and the eventX device will be accessible via the static device name /dev/nimbus

