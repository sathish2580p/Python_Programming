print("*")
# output:
# *

print("*")
print("*")
# output:
# *
# *

for i in range(5):
    print('*')
# output:
# *
# *
# *
# *
# *


for i in range(5):
    print('*',end=' ')
# output:
# * * * * * 

row=int(input('row: '))
for i in range(row):
    print('*',end=' ')
# output:
# row: 5
# * * * * * 

# To print user input rows and columns *  

row=int(input('row: '))
col=int(input('col: '))
for i in range(row):
    for j in range(col):
        print('*',end=' ')
    print()
# output:
# row: 4
# col: 3
# * * * 
# * * * 
# * * * 
# * * * 


row=int(input('row: '))
col=int(input('col: '))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=' ')
        val+=1
    print()
# output:
# row: 4
# col: 3
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12 

row=int(input('row: '))
col=int(input('col: '))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=' ')    # for when it more than 9 again start from 1
        val+=1
        if val>9:
            val=1
    print()

# output:
# row: 5
# col: 4
# 1 2 3 4 
# 5 6 7 8 
# 9 1 2 3 
# 4 5 6 7 
# 8 9 1 2 

row=int(input('row: '))
col=int(input('col: '))
width=len(str(row*col))
val=1
for i in range(row):
    for j in range(col):
        print(str(val).zfill(width),end=' ')
        val+=1
    print()

# output::row: 4
# col: 5
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 


row=int(input('row: '))
col=int(input('col: '))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=' ')    
    print()
    val+=1
    if val>9:val=1

# output:
# row: 4
# col: 3
# 1 1 1 
# 2 2 2 
# 3 3 3 
# 4 4 4 

row=int(input('row: '))
col=int(input('col: '))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=' ')  
        val+=1  
    print()
    val=1
# output:
# row: 4
# col: 3
# 1 2 3 
# 1 2 3 
# 1 2 3 
# 1 2 3

# pattern  for square and rectangle

row=int(input('row: '))
col=int(input('col: '))
for i in range(row):
     val=1 
     for j in range(col):
        print(val,end=' ') 
        
     val+=1
     print()
# output:   
# row: 4
# col: 3
# 1 1 1 
# 1 1 1 
# 1 1 1 
# 1 1 1 

row=int(input('row: '))
col=int(input('col: '))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=' ')    
    print()
    val+=1
# output:   
# row: 4
# col: 3
# 1 1 1 
# 2 2 2 
# 3 3 3 
# 4 4 4 

row=int(input('row: '))
col=int(input('col: '))
val=0
for i in range(row):
    for j in range(col):
        val+=1
        print(val, end=' ')
    print()

# output:
# row: 4 
# col: 3
# 1 2 3 
# 4 5 6 
# 7 8 9 
# 10 11 12 

row = int(input("row: "))
col = int(input("col: "))
val = 1
for i in range(row):
    for j in range(col):
        print(val, end=" ")
        val += 1
    print()
#output:
# row: 4
# col: 3
# 1 2 3 
# 4 5 6 
# 7 8 9 
# 10 11 12 


row=int(input('row: '))
col=int(input('col: '))
val=9
for i in range(row):
    for j in range(col):
        print(val,end=' ')
        val-=1
    print()
# output:
# row: 4
# col: 3
# 9 8 7 
# 6 5 4 
# 3 2 1 
# 0 -1 -2 