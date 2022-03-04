Motor Examples
==============

To control motor/servo movement with a game controller (In my case the Steelseries Nimbus),
You need to use data from input events and values from the game controller and translate it 
to something the motor library understands. I use the Raspberry Pi LEGO buildhat and in this
example I only want to use the left analog joystick:

| Key/button                   | ecode | analog/digital | value min | value max |
| ---------------------------- | ----- | -------------- | --------- | --------- |
| Joystick-left ( Left/Right ) | 00 | analog | -127 | 127 |
| Joystick-left ( Up/Down) | 01 | analog | -127 | 127 |


# Moving forwards and  backwards #
As you can see, the value range starts at -127 and ends at 127. The lego buildhat library allows
you to choose the powerlevel and direction:

1. -100 to -1: 	Motor powerlevel (speed) in direction 1.
2. 1 to 100: 	Motor powerlevel (speed) in direction 2.


# Steering #
For steering, the motor needs to operate like a servo. The motor position needs to be set 
on a specific angle. Compatible LEGO motors have a resolution of 1 degree. You need to think about a range  
(maximum degrees left and maximum degrees right). This maximum has to correspond to the value range of  -127 to 127.
Of course, a full circle has 360 degrees. 360 is also the 0 degree position. 
For the sake of simplicity I just used the input values directly as degrees. Keep in mind that value  -127 corresponds to 
a 233 degrees motor position (360 + -127)  . Configure your motor to change position by the quickest/shortest route 
to make sure the motor turns left if you go left and turns right if you want to go right.

Be aware of your gear configuration. A different transmission between the gears leads to different travel distance.


1. 0 degrees (straigh on )
2. 233 degrees (max left )
3. 127 degrees (max right )



