import csv
from datetime import datetime

# This function converts inches to centimeters
def convertData(var1):
    conv = (var1-32)*5/9
    return conv

# This function prompts the user for input (date and length in inches) and writes each entry to a CSV file called "ZooData.csv"
def getInput():
    try:
        i = 0
        x = int(input("How many entries are being input?: "))
        while i < x:
            date = str(input("Enter a date: "))
            temp = int(input("Enter the temperature in Fahrenheit: "))
            # Calling the convertData function, expecting an integer return value.
            tempC = convertData(temp)
            data_string = f"{date},{temp},{tempC}"
            # Calling insertData to save the data
            insertData("ZooData.csv", data_string)
            i += 1
    except Exception as e:
        print(f"The following error has occurred: {e}")

# This function inserts the given comma-separated string into a CSV file.
def insertData(path, string):
    try:
        date = datetime.now()
        data = string
        with open(path, "a", newline='') as csvfile:
            csvfile.write(string + "\n")
            print(f"The following data was saved at {date}: {data}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# This function reads and displays the contents of a CSV file.
# It prints the contents along with the file path to the user.
def viewData(path):
    try:
        data = []
        with open(path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                data.append(row)
        print(f"Contents of {path}:")
        for entry in data:
            print(entry)
    except Exception as e:
        print(f"The following error occurred while reading the file: {e}")

# Main program flow
print("derave1577 Spreadsheet Automation Menu")
print("")
print("Choose a number from the following programs")
options = ["1. Input Data", "2. View Current Data", "3. Generate Report"]
for i in options:
    print(i)

# The next line retrieves the inputted option and stores it into the variable x.
x = int(input())

match x:
    case 1:
        print("")
        print('You selected input data.')
        getInput()
    case 2:
        print("")
        print('You selected view current data.')
        print('The date and time is', str(datetime.now()))
        viewData("ZooData.csv")
    case 3:
        print("")
        print('You selected generate report.')
        print('The date and time is', str(datetime.now()))
        print("This feature is not currently available.")
    case _:
        print("")
        print("Invalid input")
