import time
import random


def thestart():
    selection = input("which place do you want to enter?\n1 : calculator\n2 : random number generator\n")
    startcorrect = True
    if selection == ("1"):
        calculator()
    elif selection == ("2"):
        rng()
    else:
        thestart()


def calculator():
    calc_contin = int(1)
    while calc_contin == 1:
        firstnumcorrect = bool(False)
        secondnumcorrect = bool(False)
        operationcorrect = bool(False)
        while firstnumcorrect == False:
             try:
                firstnum = int(input("what is your first number?\n"))
                firstnumcorrect = True
             except ValueError:
                 time.sleep(0.5)
                 print("invalid response")
                 time.sleep(0.5)
    
        while secondnumcorrect == False:
             try:
                secondnum = int(input("what is your second number?\n"))
                secondnumcorrect = True
             except ValueError:
                 time.sleep(0.5)
                 print("invalid response")
                 time.sleep(0.5)

        while operationcorrect == False:
            operation = str(input("what operation do you want to do?\n1 : multiply\n2 : divide\n3 : add\n4 : subtract\n"))

            if operation == "multiply" or operation == "1":
                print(firstnum,"multiplied by",secondnum,"=",firstnum*secondnum)
                operationcorrect = True
            elif operation == "divide" or operation == "2":
                print(firstnum,"divided by",secondnum,"=",firstnum/secondnum)
                operationcorrect = True
            elif operation == "add" or operation == "3":
                print(firstnum,"add",secondnum,"=",firstnum+secondnum)
                operationcorrect = True
            elif operation == "subtract" or operation == "4":
                print(firstnum,"take away",secondnum,"=",firstnum-secondnum,)
                operationcorrect = True
            else:
                time.sleep(0.5)
                print("invalid response")
                time.sleep(0.5)

        while True:
            try:
                calc_contin = int(input("would you like to continue? press 1.\nwould you like to leave the calculator? press 2.\n"))
                break
            except ValueError:
                print("invalid response")
                
        if calc_contin == 2:
            print("returing to menu")
            time.sleep(0.5)
            thestart()


def rng():
    gamblednumber = int
    rngcontin = int(1)

    lowercorrect = bool(False)
    highercorrect = bool(False)
    chosenrngcorrect = bool(False)
    continuecorrect = bool(False)

    while rngcontin == 1:
        while lowercorrect == False:
            try:
                lowerbound = int(input("enter the lowest number possible"))
                lowercorrect = True
            except ValueError:
                print("invalid response")


        while highercorrect == False:
            try:
                higherbound = int(input("enter the highest number possible"))
                if higherbound < lowerbound:
                    print("invalid response")
                else:
                    highercorrect = True
            except ValueError:
                print("invalid response")


        while chosenrngcorrect == False:
            try:
                chosenrngnum = int(input("enter the number you wish to recieve"))
                if chosenrngnum > higherbound or chosenrngnum < lowerbound:
                    print("invalid response")
                else:
                    chosenrngcorrect = True
            except ValueError:
                print("invalid response")


        time.sleep(0.5)
        while gamblednumber != chosenrngnum:
            gamblednumber = random.randint(lowerbound, higherbound)
            print (gamblednumber)

        while continuecorrect == False:
            try:
                rngcontin = int(input("would you like to continue? press 1.\nwould you like to leave the random number generator? press 2.\n"))
                continuecorrect = True
                if rngcontin == 1:
                    rng()
                if rngcontin == 2:
                    print("returning to menu")
                    time.sleep(0.5)
                    thestart()
            except ValueError:
                print("invalid response")


verystartcorrect = bool(False)

while verystartcorrect == False:
    try:
        contin = str(input("welcome to this compilation of random things!\ntype y/n to start!!!\n"))

        if contin == "y":
            print ("entering...")
            time.sleep(0.5) # dramatic effect
            thestart()
            
        elif contin == "n":
            print ("goodbye!!!")
            exit()

        else:
            print ("invalid response")
    except ValueError:
        print("invalid response")
