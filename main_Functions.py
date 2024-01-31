import globals

def printMenu():
    count = 1
    print("What would you like to do?")
    for options in globals.menuOptions:
        print(str(count)+".", options)
        count = count + 1
