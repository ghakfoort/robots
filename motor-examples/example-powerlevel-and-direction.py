from evdev import InputDevice, categorize, ecodes
from buildhat import Motor

motora = Motor('A')
gamepad = InputDevice('/dev/nimbus')
 
for event in gamepad.read_loop():
    keyevent = categorize(event)
    #print(event)

    # Every buttonpress on an input device can be seen as an event. 
    # Every input event has a specific event code.
    if event.code == 1 and event.value != 0:
        print("Left joystick forward/backwards pressed")
        print("Speed:")
        print(event.value)

        # The value 0 isn't really the value of an event because the joystick is not touched at all.
        # To stop the motor, values near 0 are used
        if event.value >= -9 and event.value <= 9:
            motora.stop()

        #the joysticks on the Steelseries Nimbus have values between -127 and 127. 
        #this needs to be translated to the powerlevel range and direction (negative or positive values) 
        #the LEGO motor is used to work with (-100 to 100 )
        if event.value <= 127 and event.value >= -127:
            print(round((event.value/127)*100))
            motora.start(speed=(round((event.value/127)*100)))
            continue
            
        else:
            print("illegal or unknown speed")
