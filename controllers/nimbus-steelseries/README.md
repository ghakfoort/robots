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

E-codes
-------

| Button | Ecode | Type | Value-min | Value-max |
| ------ | ----- | ---- | --------- | --------- |
| Menu   | 172   | digital | NA | NA |
| A      | 304   | digital | NA | NA |
| B      | 305   | digital | NA | NA |
| X      | 306   | digital | NA | NA |
| Y      | 307   | digital | NA | NA |
| L1	 | 308   | digital | NA | NA |
| R1	 | 309   | digital | NA | NA |
| L2	 | 310   | analog  | -127 | 127 |
| R2	 | 311	 | analog  | -127 | 127 |
| Joystick-left ( Left/Right ) | 00 | analog | -127 | 127 |
| Joystick-left ( Up/Down) | 01 | analog | -127 | 127 |
| Joystick-left ( Press ) | 04 | digital | NA | NA |
| Joystick-right (Left/Right ) | 02 | analog | -127 | 127 |
| Joystick-right (Up/Down ) | 03 | analog | -127 | 127 |
| Joystick-right ( Press ) | 05 | digital | NA | NA |

Unfortunately i was not yet able to identify the corresponding ecodes of the 4 buttons of the directional pad.
 

