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
    case 2:
        print("")
        print('You selected view current data.')
        print('The date and time is',str(datetime.now()))
    case 3:
        print("")
        print('You selected generate report.')
        print('The date and time is',str(datetime.now()))
    case _:
        print("")
        print("Invalid input")
