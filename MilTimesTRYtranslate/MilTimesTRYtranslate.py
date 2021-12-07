from module1 import *
while True:
    menu=input("Tranlate - T\nNew word - N\nCheck and correct - C\nExit - E\nYou have to decide what u want:  ")
    if menu.upper()=="T":
        T=translate()
    elif menu.upper()=="N":
        N=new_word()
    elif menu.upper()=="C":
        l=int(input("Do u see mistakes? 1-yes or 2-no: "))
        if l==2:
            print("Oh, thats cool!")
        elif l==1:
            C=correct()
    elif menu.upper()=="E":
        print("Bye bye, see ya next time!")
        exit(0)
