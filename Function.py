# Define rows as lists
from tabulate import tabulate

headers = ["Category", "Task", "Done", "CreatedAT", "CompletedAt"]

def todo(PrepData):
    print(tabulate(PrepData, headers=headers, tablefmt="grid"))

def todo_manual(PrepData):

    length=[]
    result=[]
    a=0
    while (a<len(PrepData)) :
        length.append([len(PrepData[a][0]),len(PrepData[a][1]),len(PrepData[a][2]),len(str(PrepData[a][3])),len(str(PrepData[a][4]))])
        a+=1
    total=0
    
    for i in range(len(headers)) :
        max=len(headers[i])
        for j in range(len(length)) :
            if length[j][i]>max :
                max=length[j][i]
        result.append(max)
        total+=max
        max=0   
    print(result)
     
    total+=2*(((int(length[0][i])-len(headers[i]))//2))
    print('='*(total+19))
    print('||',end=' ')
    for i in range(len(headers)) :
        print(' '*((int(result[i])-len(headers[i]))//2),end='')
        print(f"{headers[i]}", end=' ')
        print(' '*((int(result[i])-len(headers[i]))//2),end='')
        print(' ||',end=' ')
    print()  
    
    for i in range(len(PrepData)) :
        print('='*(total+19))
        print('||',end=' ') 
        for j in range(len(PrepData[i])) :
            print(' '*((int(result[j])-len(str(PrepData[i][j])))//2),end='')
            print(f"{PrepData[i][j]}", end=' ')
            print(' '*((int(result[j])-len(str(PrepData[i][j])))-((int(result[j])-len(str(PrepData[i][j])))//2)),end='')
            print(' ||',end=' ')
    print()        
    print('='*(total+19))

# Define headers
