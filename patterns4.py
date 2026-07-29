#1)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print(val, end=' ')
            val+=1
        else:
            print(' ', end=' ')
    print()
#output:
# enter: 5
#         1 
#       2   
#     3     
#   4       
# 5

#2)
n=int(input('enter: '))
val=ord('A')
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print(chr(val), end=' ')
            val+=1
        else:
            print(' ', end=' ')
    print()

#output:
# enter: 5
#         A 
#       B   
#     C     
#   D       
# E  

#3)
n=int(input('enter: '))
val=4
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print(val, end=' ')
            val-=1
        else:
            print(' ', end=' ')
    print()
#output:
# enter: 5
#         4 
#       3   
#     2     
#   1       
# 0  

#4)
n=int(input('enter: '))
val=ord('Z')
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print(chr(val), end=' ')
            val-=1
        else:
            print(' ', end=' ')
    print()

#output:
# enter: 5
#         Z 
#       Y   
#     X     
#   W       
# V  

#5)
n=int(input('enter: '))
val=ord('D')
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            print(chr(val), end=' ')
            val-=1
        else:
            print(' ', end=' ')
    print()

#output:
# enter: 4
#       D 
#     C   
#   B     
# A 

#6)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)==n-1:
            if i%2==0:
                print(val, end=' ')
                val+=1
            else:
                 print('*', end=' ')
        else:
                print(' ', end=' ')
    print()

#output:
# enter: 4
#       1 
#     *   
#   2     
# *  

#7)
n=int(input('enter: '))
val=ord('A')
for i in range(n):
    
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val), end=' ')
        else:
            print(' ', end=' ')
    print()
    val+=1
#output:
# enter: 4
#       A 
#     B B 
#   C C C 
# D D D D 

#8)
n=int(input('enter: '))
for i in range(n):
    val=ord('A')
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val), end=' ')
            val+=1
        else:
            print(' ', end=' ')
    print()

# enter: 4
#       A 
#     A B 
#   A B C 
# A B C D 

#9)
n=int(input('enter: '))
val=ord('D')
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val), end=' ')
        else:
            print(' ', end=' ')
    print()
    val-=1
#output:
# enter: 4
#       D 
#     C C 
#   B B B 
# A A A A 

#10)
n=int(input('enter: '))
for i in range(n):
    val=ord('D')
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val), end=' ')
            val-=1
        else:
            print(' ', end=' ')
    print()

#output:
# enter: 4
#       D 
#     D C 
#   D C B 
# D C B A 

#11)
n=int(input('enter: '))
for i in range(n):
    val=ord('Z')
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val), end=' ')
            val-=1
        else:
            print(' ', end=' ')
    print()

#output:
# enter: 4
#       Z 
#     Z Y 
#   Z Y X 
# Z Y X W

#12)
n=int(input('enter: '))
val=ord('Z')
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(chr(val), end=' ')
            
        else:
            print(' ', end=' ')
    print()
    val-=1
#output:
# enter: 4
#       Z 
#     Y Y 
#   X X X 
# W W W W 

#13)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(val, end=' ') 
        else:
            print(' ', end=' ')
    print()
    val+=1
#output:
# enter: 4
#       1 
#     2 2 
#   3 3 3 
# 4 4 4 4 

#14)
n=int(input('enter: '))
for i in range(n):
    val=1
    for j in range(n):
        if (i+j)>=n-1:
            print(val, end=' ') 
            val+=1
        else:
            print(' ', end=' ')
    print()
#output:
# enter: 4
#       1 
#     1 2 
#   1 2 3 
# 1 2 3 4 

#15)
n=int(input('enter: '))
val=4
for i in range(n):
    for j in range(n):
        if (i+j)>=n-1:
            print(val, end=' ') 
        else:
            print(' ', end=' ')
    print() 
    val-=1 
#output:
# enter: 4
#       4 
#     3 3 
#   2 2 2 
# 1 1 1 1 

#16)
n=int(input('enter: '))
for i in range(n):
    val=4
    for j in range(n):
        if (i+j)>=n-1:
            print(val, end=' ') 
            val-=1
        else:
            print(' ', end=' ')
    print() 

#output:
# enter: 4
#       4 
#     4 3 
#   4 3 2 
# 4 3 2 1 

#17)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(val, end=' ') 
        else:
            print(' ', end=' ')
    print() 
    val+=1
#output:
# enter: 4
# 1 1 1 1 
# 2 2 2   
# 3 3     
# 4  

#18)    
n=int(input('enter: '))
for i in range(n):
    val=1
    for j in range(n):
        if (i+j)<=n-1:
            print(val, end=' ') 
            val+=1
        else:
            print(' ', end=' ')
    print() 
# output:
# enter: 4
# 1 2 3 4 
# 1 2 3   
# 1 2     
# 1   

#19)
n=int(input('enter: '))
for i in range(n):
    val=4
    for j in range(n):
        if (i+j)<=n-1:
            print(val, end=' ') 
            val-=1
        else:
            print(' ', end=' ')
    print()
# output:
# enter: 4
# 4 3 2 1 
# 4 3 2   
# 4 3     
# 4 

#20)
n=int(input('enter: '))
for i in range(n):
    val=ord('A')
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val), end=' ') 
            val+=1
        else:
            print(' ', end=' ')
    print()
#output:
# enter: 4
# A B C D 
# A B C   
# A B     
# A   

#21)
n=int(input('enter: '))
val=ord('A')
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val), end=' ') 
        else:
            print(' ', end=' ')
    print()
    val+=1
#output:
# enter: 4
# A A A A 
# B B B   
# C C     
# D 

#22)
n=int(input('enter: '))
val=ord('Z')
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val), end=' ') 
        else:
            print(' ', end=' ')
    print()
    val-=1
#output:
# enter: 4
# Z Z Z Z 
# Y Y Y   
# X X     
# W 

#23)
n=int(input('enter: '))
for i in range(n):
    val=ord('Z')
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val), end=' ')
            val-=1
        else:
            print(' ', end=' ')
    print()
#output:
# enter: 4
# Z Y X W 
# Z Y X   
# Z Y     
# Z  

#24)
n=int(input('enter: '))
val=ord('D')
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val), end=' ')   
        else:
            print(' ', end=' ')
    print()
    val-=1
#output:
# enter: 4
# D D D D 
# C C C   
# B B     
# A 

#25)
n=int(input('enter: '))
for i in range(n):
    val=ord('D')
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val), end=' ') 
            val-=1  
        else:
            print(' ', end=' ')
    print()
#output:
# enter: 4
# D C B A 
# D C B   
# D C     
# D 

#26)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n):
        if (i+j)<=n-1:
            if j%2==0:
                print(val, end=' ') 
                val+=1 
            else:
                print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
 #output:
 # enter: 4
# 1 * 2 * 
# 3 * 4   
# 5 *     
# 6     

#27)
n=int(input('enter: '))
val=ord('A')
for i in range(n):
    
    for j in range(n):
        if (i+j)<=n-1:
            print(chr(val), end=' ') 
            val+=1 
        else:
            print(' ', end=' ')
    print()
#output:
# enter: 4
# A B C D 
# E F G   
# H I     
# J    
    