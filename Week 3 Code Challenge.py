import datetime
x = datetime.datetime.now()
print("derave1577", x)

# Function that forces the variable to an integer and asks if it's even or odd.
def evenOrOdd(num1):
    num1 = int(num1)
    if (num1 % 2):
        print(f'{num1} is odd.')
    else:
        print(f'{num1} is even.')

list = [3,14,23,30]

for i in list:
    evenOrOdd(i)
