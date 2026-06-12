from tabulate import tabulate
from Function import *
import datetime


count=int(input("How many to-do items do you want to add? "))
number=count
PrepData=[[]]
for j in range(count):
    
    for i in range(len(headers)):
        if headers[i] == "Done":
            PrepData[j].append('Done' if (input(f"{headers[i]} (True/False): "))=='True' else 'Not Done')
       
        else:
            PrepData[j].append(input(f'{headers[i]}: '))

    number-=1
todo(PrepData)

# Print the table with a grid formatting style
# print(tabulate(data, headers=headers, tablefmt="grid"))

