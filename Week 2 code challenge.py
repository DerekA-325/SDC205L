import datetime
x = datetime.datetime.now()
print("derave1577", x)

list = [60,33,88,3,7,9,22]
print(list)

largest = 0
smallest = 99999999

for i in list:
    if i > largest:
        largest = i
    else:
        largest = largest
i = 0
for i in list:
    if i < smallest:
        smallest = i
    else:
        smallest = smallest
print(f'The largest number is: {largest}')
print(f'The smallest number is: {smallest}')
