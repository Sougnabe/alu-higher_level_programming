#!/usr/bin/python3
def islower(c):
    # Vérifie si le caractère c est en minuscule
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
if _name_ == "_main_":
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
