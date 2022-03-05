from evdev import InputDevice, categorize, ecodes
from buildhat import Motor

motora = Motor('A')
gamepad = InputDevice('/dev/nimbus')
 
for event in gamepad.read_loop():
    keyevent = categorize(event)
    #print(event)


    if event.code == 1 and event.value != 0:
        print("Left joystick forward/backwards pressed")
        print("Speed:")
        print(event.value)

        if event.value == 0:
            motora.stop()
            
        if event.value <= 127 and event.value >= -127:
            print(round((event.value/127)*100))
            motora.start(speed=(round((event.value/127)*100)))
            continue
            
        else:
            print("illegal or unknown speed")
