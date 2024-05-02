genArray = [
    ["1554","USA","56"],
    ["75892","Palestine","100"],
    ["3453","Haiti","4"]
    ]

choice = int(input("Do you wish to  1)add a generator or 2)check on the generator? "))


def addGen():
    genCode = input("Enter serial no. ")
    genLocation = input("Enter location: ")
    genPercentage = input("Enter battery percentage: ")
    genArrayStr = [genCode,genLocation,genPercentage]
    genArray.append(genArrayStr)
    print("Added!")
    choice2 = int(input("Do you wish 1) add a generator, 2) check generator or 3) leave? "))
    if choice2 == 1:
        addGen()
    elif choice2 == 2:
        checkGen()
    else:
        quit()

def checkGen():
    choice3 = int(input("Do you want to 1)check generators or 2)check battery life? "))
    
    if choice3 == 1: #branch on gen or battery -- check
        choice3_1 = int(input("Do you want to check 1) all generators or 2)specific generator? "))
        
        if choice3_1 == 1: #branch on all or specific -- all 
            print("All generators...")
            print(genArray)
            
            choice5_1 = int(input("Do you want to check 1)add a generator or 2)check on the generator or 3) quit? "))
            if choice5_1 == 1:
                addGen()
            elif choice5_1 == 2:
                checkGen()
            else:
                quit()
                
        else:  #branch on all or specific -- specific 
            serialNoCheck = input("Enter serial No. ")
            for i in range (len(genArray)):
                if serialNoCheck == genArray[i][0]:
                    print("Found in records! " + str(genArray[i]))
                    choice5_2 = int(input("Do you want to check 1)add a generator or 2)check on the generator or 3) quit? "))
                    if choice5_2 == 1:
                        addGen()
                    elif choice5_2 == 2:
                        checkGen()
                    else:
                        quit()

                else:
                    i = i + 1

                    
    else: #brancj for gen or battery - battery
        serialNoCheckBattery = input("Enter serial No.")
        serialNoArray = [genArray[0] for genArray in genArray]
        for i in range(len(serialNoArray)):
            if serialNoCheckBattery == serialNoArray[i]:
                
                batteryArray = [genArray[2] for genArray in genArray]
                batteryValue = batteryArray[i]
            else:
                i = i + 1            
        batteryTime = 30 * (int(batteryValue)/100) #finds no. of hours left
        powerLitres = 6 * (int(batteryValue)/100)   #finds how much diesel is left
        batteryTimeRounded = round(batteryTime, 1)
        powerLitresRounded = round(powerLitres, 2)
        print("You have " + str(batteryTimeRounded) + " hours left")
        print("You have " + str(powerLitresRounded) + " litres left")
        choice4 = int(input("Do you wish 1) add a generator, 2) check generator or 3) leave? "))
        if choice4 == 1:
            addGen()
        elif choice4 == 2:
            checkGen()
        else:
            quit()
 
if choice == 1:
    print(addGen())
else:
    print(checkGen())
