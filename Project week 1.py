print('derave1577 Spreadsheet Automation Menu')

print('1. Input Data')
print('2. View Current Data')
print('3. Generate Report')

# The next line retrieves the inputted option and stores it into the variable x.
x = int(input('Please type the number for the menu option you choose: '))

from datetime import datetime

match x:
    case 1:
        print('You selected input data.')
        print('The date and time is',str(datetime.now()))
    case 2:
        print('You selected view current data.')
        print('The date and time is',str(datetime.now()))
    case 3:
        print('You selected generate report.')
        print('The date and time is',str(datetime.now()))
