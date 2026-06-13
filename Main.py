from tabulate import tabulate
from Function import *
from datetime import datetime


count=int(input("How many to-do items do you want to add? "))
number=count
PrepData=[[]]
for j in range(count):
    
    for i in range(len(headers)):
        if headers[i] == "Done":
            PrepData[j].append('Done' if (input(f"{headers[i]} (True/False): "))=='True' else 'Not Done')
        elif headers[i] == "CreatedAT":
            try :
                PrepData[j].append(datetime.strptime(input(f"{headers[i]} (YYYY-MM-DD): "), "%Y-%m-%d"))
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                exit()
        elif headers[i] == "CompletedAt":
            try :
                PrepData[j].append(datetime.strptime(input(f"{headers[i]} (YYYY-MM-DD): "), "%Y-%m-%d"))
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                exit()
        else :
            PrepData[j].append(input(f"{headers[i]}: "))

    number-=1
todo(PrepData)
todo_manual(PrepData)

# Print the table with a grid formatting style
# print(tabulate(data, headers=headers, tablefmt="grid"))

