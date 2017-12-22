import random


def compare(gennum, guessnum):
    return gennum - guessnum


def main():
    usercont = True
    while usercont:
        try:
            gennum = random.randint(1, 10)
            corguess = False
            while not corguess:
                try:
                    validinput = False
                    while not validinput:
                        try:
                            guessnum = int(input("Please guess a number between 1 and 10: "))
                            if (guessnum > 10 or guessnum < 1):
                                print("Invalid Entry;")
                                continue
                            validinput = True
                        except ValueError:
                            print("Invalid Entry; Please enter a number between 1 and 10")
                except ValueError:
                    print("Invalid Entry; Please enter a number between 1 and 10")
                    
                compareval = compare(gennum, guessnum)

                if (compareval <= -3 or compareval >= 3):
                      print("You're pretty cold; try again")
                      continue

                elif (-3 < compareval < -1 or 1 < compareval < 3):
                    print("You're getting warm; Try again")
                    continue

                elif ((compareval >= -2 and compareval < 0) or (compareval <=2 and compareval > 0)):
                    print("You're very close!")
                    continue

                else:
                    print("You've got it!")
                    corguess = True
                    break
        except ValueError:
            print("Invalid Entry; Please try again")
        contvalidinput = False
        while not contvalidinput:
                try:
                    prefcont = int(input("Would you like to continue? 1. Yes 2. No: "))
                    if (prefcont != 1 and prefcont != 2):
                        print("Invalid Selection; Please enter 1 or 2")
                        continue
                    elif (prefcont == 2):
                        contvalidinput = True
                        usercont = False
                        print("Thanks for playing!")
                        break
                    else:
                        break
                        
                except ValueError:
                    print("Invalid Selection; try again")
        continue


main()


