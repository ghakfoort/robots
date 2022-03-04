
#vposjsleft = Vertical POSition JoyStick left
def calcSpeed(vposjsleft):
    if vposjsleft <= 127 and vposjsleft >= -127:
        print(round((vposjsleft/127)*100))
    else:
        print("illegal or unknown speed")

calcSpeed(-100)
