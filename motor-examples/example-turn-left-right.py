#hposjsleft = Horizontal POSition JoyStick left
def calcSteering(hposjsleft):
    if hposjsleft <= 127 and hposjsleft > 0:
        print(round((hposjsleft/127)*100))
        print("absolute degrees position right")
    elif hposjsleft >= -127 and hposjsleft < 0:
        print(round(360 + (hposjsleft/127)*100))
        print("absolute degrees position left")
    elif hposjsleft == 0:
        print(hposjsleft)
        print("straight")
    else:
        print("Illegal or unknown steering angle motor position")

    
    
calcSteering(126)
