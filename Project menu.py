import csv
from datetime import datetime
from openpyxl import Workbook
from openpyxl.chart import LineChart, BarChart, Reference

# This function converts Fahrenheit to Celsius
def convertData(var1, data_type="Fahrenheit"):
    if data_type == "Fahrenheit":
        return (var1 - 32) * 5.0 / 9.0
    else:
        return var1  # If no conversion, return the original value (for Celsius)

# This function prompts the user for input (date and temperature in Fahrenheit) and writes each entry to a CSV file called "ZooData.csv"
def getInput():
    try:
        i = 0
        x = int(input("How many entries are being input?: "))
        while i < x:
            date = str(input("Enter a date: "))
            temp = float(input("Enter a temperature in Fahrenheit: "))
            # Calling the convertData function to convert the temperature to Celsius
            tempC = convertData(temp, "Fahrenheit")
            # Prepare the data string for insertion into the CSV
            dataString = f"{date},{temp},{tempC}"
            # Calling insertData to save the data
            insertData("ZooData.csv", dataString)
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
def viewData(path):
    try:
        data = []
        with open(path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                data.append(row)
        # Display all entries in the CSV file
        print(f"Contents of {path}:")
        for entry in data:
            print(entry)
    except Exception as e:
        print(f"The following error occurred while reading the file: {e}")

# This function creates a chart (line or bar) and saves it to an Excel file.
def createChart(path, chartType):
    try:
        # Ask the user for the data source (initial or converted)
        dataSource = input("Do you want to use initial data (Fahrenheit) or converted data (Celsius)? ")
        
        if dataSource not in ['initial', 'converted']:
            print("Invalid choice! Please enter either 'initial' or 'converted'.")
            return

        # Open the CSV file and extract data
        dates = []
        initialData = []
        convertedData = []

        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                dates.append(row[0])
                initialData.append([float(row[1])])
                convertedData.append([float(row[2])])

        if dataSource == 'initial':
            chartData = initialData
        else:
            chartData = convertedData

        # Create an Excel workbook and add the data
        wb = Workbook()
        ws = wb.active
        ws.append(['Date', 'Temperature'])

        # Write the data into the Excel sheet
        i = 0
        for date in dates:
            ws.append([date, chartData[i][0]]) 
            i += 1


        # Create the chart
        if chartType == 'line':
            chart = LineChart()
        elif chartType == 'bar':
            chart = BarChart()
        else:
            print("Invalid chart type! Please enter 'line' or 'bar'.")
            return

        # Add data to the chart
        data = Reference(ws, min_col=2, min_row=1, max_row=len(dates)+1, max_col=2)
        categories = Reference(ws, min_col=1, min_row=2, max_row=len(dates)+1)
        chart.add_data(data)
        chart.set_categories(categories)

        # Add the chart to the sheet
        ws.add_chart(chart, "E5")

        studentId = "derave1577"
        currentDate = datetime.now()
        chart.title = f"{studentId} {currentDate}"

        # Save the Excel file
        wb.save("final.xlsx")
        print("Chart created and saved as 'final.xlsx'.")
    except Exception as e:
        print(f"An error occurred while creating the chart: {e}")

# This function generates a report by prompting the user to choose the chart type and then calls the createChart function to generate the chart.
def generateReport(path):
    try:
        # Ask the user for the chart type (line or bar)
        chartType = input("Which type of chart would you like to create? (line or bar): ")

        if chartType not in ['line', 'bar']:
            print("Invalid chart type! Please enter 'line' or 'bar'.")
            return

        # Call the createChart function to generate the chart
        createChart(path, chartType)
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

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
        generateReport("ZooData.csv")
    case _:
        print("")
        print("Invalid input")

