import datetime
# The purpose of this application is to calculate the user's age in 5 years,
# calculate double the user's age, and display the current date and time.

id = str(input('Enter student ID: '))
age = int(input('Enter age: '))
x = datetime.datetime.now()

print(f'{id}')
print(f'Your age in 5 years: {age + 5}')
print(f'Your age doubled: {age * 2}')
print(x)
