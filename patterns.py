row=int(input('row: '))
col=int(input('col: '))
val=row
if val>9:
    val=1
for i in range(row):
    for j in range(col):
        print(val,end=' ')
    print()
    val-=1
    if val<1:val=9
# output:
# row: 4
# col: 3
# 4 4 4 
# 3 3 3 
# 2 2 2 
# 1 1 1 


row=int(input('row: '))
col=int(input('col: '))
for i in range(row):
    val=col
    for j in range(col):
        print(val,end=' ')
        val-=1
    print()
# output:
# row: 4
# col: 3
# 3 2 1 
# 3 2 1 
# 3 2 1 
# 3 2 1 


row=int(input('row: '))
col=int(input('col: '))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=' ')
        val+=1
        if ord('Z'):var='A'
    print()
# output:
# row: 4
# col: 3
# A B C 
# D E F 
# G H I 
# J K L 


row=int(input('row: '))
col=int(input('col: '))
val=65
for i in range(row):
    for j in range(col):
        print(chr(val),end=' ')
        val+=1
        if chr(122):var=65
    print()
# output:
# row: 4
# col: 3
# A B C 
# D E F 
# G H I 
# J K L 


row=int(input('row: '))
col=int(input('col: '))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=' ')
    print()
    val+=1
    if ord('Z'):var='A'   
# output:
# row: 4
# col: 3
# A A A 
# B B B 
# C C C 
# D D D  
   


row=int(input('row: '))
col=int(input('col: '))
for i in range(row):
    val=ord('A')
    for j in range(col):
        print(chr(val),end=' ')
    print()
    val+=1
    if ord('Z'):var='A'  
# output:  
# row: 5
# col: 4
# A A A A 
# A A A A 
# A A A A 
# A A A A 
# A A A A 

row=int(input('row: '))
col=int(input('col: '))
val=ord('A')+row-1
for i in range(row):
    for j in range(col):
        print(chr(val),end=' ')
    print()
    val-=1
    if val<ord('A'):val=ord('Z')
# output:
# row: 5
# col: 4
# E E E E 
# D D D D 
# C C C C 
# B B B B 
# A A A A


row=int(input('row: '))
col=int(input('col: '))
val=ord('A')+row-1
for i in range(row):
    for j in range(col):
        print(chr(val),end=' ')
    print()
    val-=1
    if val<ord('A'):ord('A')+row-1
# output:
# row: 5
# col: 4
# D C B A 
# D C B A 
# D C B A 
# D C B A 
# D C B A 


row=int(input('row: '))
col=int(input('col: '))
for i in range(row):
    val=ord('A')+col-1
    for j in range(col):
        print(chr(val),end=' ')
        val-=1
    print()
    if val<ord('A'):ord('A')+row-1
# output:
# row: 5
# col: 4
# D C B A 
# D C B A 
# D C B A 
# D C B A 
# D C B A 

n=5
for i  in range(1,n+1):
    print(' '*(n-i)+'*' *i)
# output:
#     *
#    **
#   ***
#  ****
# *****

n=int(input('enter: '))
for i  in range(1,n+1):
    print(str(i) *i+(n-i)*' ')

# output:
# enter: 4
# 1   
# 22  
# 333 
# 4444

row = int(input("Enter rows: "))
col = int(input("Enter cols: "))
for i in range(row):
    val = ord('Z') - i
    for j in range(col):
        print(chr(val), end=' ')
    print()
# output:
# Enter rows: 4
# Enter cols: 3
# Z Z Z 
# Y Y Y 
# X X X 
# W W W 


row = int(input("Enter rows: "))
col = int(input("Enter cols: "))
for i in range(row):
    val = ord('Z')
    for j in range(col):
        print(chr(val), end=' ')   
        val-=1
    print()
# output:
# Enter rows: 5
# Enter cols: 4
# Z Y X W 
# Z Y X W 
# Z Y X W 
# Z Y X W 
# Z Y X W 
    

n= int(input("Enter: "))
val =1
for i in range(1,n+1):
    for j in range(n):
        if i%2 == 1:
            print(val, end=' ')
        else:
            print('*', end=' ')   
    if i %2 == 0:
        val+=1
    print()
# output:
# Enter: 5
# 1 1 1 1 1 
# * * * * * 
# 2 2 2 2 2 
# * * * * * 
# 3 3 3 3 3 

n = int(input("Enter n: "))
num = 1
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(num, end=" ")
            num += 1
            if num == 10:
                num = 1
        else:
            print("*", end=" ")
    print()
# output:
# Enter n: 5
# 1 * 2 * 3 
# * 4 * 5 * 
# 6 * 7 * 8 
# * 9 * 1 * 
# 2 * 3 * 4 