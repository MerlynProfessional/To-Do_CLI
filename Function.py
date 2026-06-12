# Define rows as lists
from tabulate import tabulate

headers = ["Category", "Task", "Done", "CreatedAT", "CompletedAt"]
def todo(PrepData):
    print(tabulate(PrepData, headers=headers, tablefmt="grid"))

# Define headers
