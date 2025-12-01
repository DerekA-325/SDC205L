def convertData(var1):
    conv = var1*2.54
    return conv

def getInput():
    i = 0
    x = int(input("How many entries are being input?: "))
    while (i < x):
        date = str(input("Enter a date: "))
        temp = int(input("Enter a length in inches: "))
        # Calling the convertData function, expecting an integer return value.
        tempC = convertData(temp)
        print("The following was saved on ",str(datetime.now()))
        print(f'{date}, {temp}in, {tempC}cm')
        i = i+1

print("derave1577 Spreadsheet Automation Menu")
print("")
print("Choose a number from the following programs")
options = ["1. Input Data","2. View Current Data","3. Generate Report"]
for i in options:
    print(i)
    
# The next line retrieves the inputted option and stores it into the variable x.
x = int(input())

from datetime import datetime

match x:
    case 1:
        print("")
        print('You selected input data.')
        print('The date and time is',str(datetime.now()))
        getInput()
    case 2:
        print("")
        print('You selected view current data.')
        print('The date and time is',str(datetime.now()))
        print("This feature is not currently available.")
    case 3:
        print("")
        print('You selected generate report.')
        print('The date and time is',str(datetime.now()))
        print("This feature is not currently available.")
    case _:
        print("")
        print("Invalid input")


        
