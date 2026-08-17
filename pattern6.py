#1)
n=int(input('enter: '))
val=1
for i in range(n):
    print('  '*(n-1-i)+(str(val)+' ')*(2*i+1))
    val+=1
#output:
# enter: 4
#         1 
#       2 2 2 
#     3 3 3 3 3 
#   4 4 4 4 4 4 4 

#1) another method
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(val, end=' ') 
    print()
    val+=1
#output:
# enter: 5
# enter: 4
#         1 
#       2 2 2 
#     3 3 3 3 3 
#   4 4 4 4 4 4 4 

#2)
n=int(input('enter: '))
for i in range(n):
    val=1
    print('  '*(n-1-i), end=' ')
    print(*range(1,2*i+2))
#output:
# enter: 4
#        1
#      1 2 3
#    1 2 3 4 5
#  1 2 3 4 5 6 7

#2)
n=int(input('enter: '))
for i in range(n):
    val=1
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(val, end=' ') 
        val+=1
    print()
#output:
# enter: 4
#       1 
#     1 2 3 
#   1 2 3 4 5 
# 1 2 3 4 5 6 7 


#3)
n=int(input('enter: '))
val=n
for i in range(n):
    print('  '*(n-1-i)+(str(val)+' ')*(2*i+1))
    val-=1
# # #output:
# # enter: 4
# #       4 
# #     3 3 3 
# #   2 2 2 2 2 
# # 1 1 1 1 1 1 1

# # 3)
n=int(input('enter: '))
val=n
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(val, end=' ') 
    print()
    val-=1
#output:
# enter: 4
#       4 
#     3 3 3 
#   2 2 2 2 2 
# 1 1 1 1 1 1 1

#4)
n=int(input('enter: '))
for i in range(n):
    val=n
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(val, end=' ') 
        val-=1
        if val<0:val=n
    print()
#output:
# enter: 4
#       4 
#     4 3 2 
#   4 3 2 1 0 
# 4 3 2 1 0 4 3 

#5)
n=int(input('enter: '))
val=ord('A')
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(chr(val), end=' ') 
        
    print()
    val+=1
# output:
# enter: 4
#       A 
#     B B B 
#   C C C C C 
# D D D D D D D 

#6)
n=int(input('enter: '))
val=ord('D')
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(chr(val), end=' ') 
        
    print()
    val-=1
    if val<ord('A'):val=ord('Z')
#output:
# enter: 4
#       D 
#     C C C 
#   B B B B B 
# A A A A A A A 

#7)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        if val==n:val=1
        print(val,end=' ') 
    print()
    val+=1
#output:
# enter: 4
# 1 1 1 1 1 1 1 
#   2 2 2 2 2 
#     3 3 3 
#       1 
    
#8)
n=int(input('enter: '))
for i in range(n):
    val=1
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print(val,end=' ') 
        val+=1
        if val>9:val=1
    print()
#op:
# enter: 4
# 1 2 3 4 5 6 7 
#   1 2 3 4 5 
#     1 2 3 
#       1 
    
#9)
n=int(input('enter: '))
val=ord('D')
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print(chr(val),end=' ')  
    print()
    val-=1
#output:
# enter: 4
# D D D D D D D 
#   C C C C C 
#     B B B 
#       A 

#10)
n=int(input('enter: '))
val=ord('A')
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(chr(val), end=' ') 
        val+=1
    print()
#op:
# enter: 4
#       A 
#     B C D 
#   E F G H I 
# J K L M N O P 

#11)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(val, end=' ') 
        val+=1
        if val>9:val=1
    print()
#op:
# enter: 4
#       1 
#     2 3 4 
#   5 6 7 8 9 
# 1 2 3 4 5 6 7

#12)
n=int(input('enter: '))
val=ord('Z')
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print(chr(val),end=' ') 
        val-=1 
    print()
#op:
# enter: 4
# Z Y X W V U T 
#   S R Q P O 
#     N M L 
#       K 
  
#13)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        if i%2==0:
            print(val, end=' ') 
        else:
            print('*',end=' ')
    print()
    if i%2==0:
        val+=1
#op:
# enter: 4
#       1 
#     * * * 
#   2 2 2 2 2 
# * * * * * * * 

#14)
n=int(input('enter: '))
val=1
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        if (i+k)%2==0:
            print(val, end=' ') 
            val+=1
        else:
            print('*',end=' ')
    print()
#op:
# enter: 4
#       1 
#     * 2 * 
#   3 * 4 * 5 
# * 6 * 7 * 8 * 

# 15)
n=int(input('enter: '))
val=ord('A')
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        if i%2==0:
            print(chr(val), end=' ') 
            val+=1
        else:
            print('*',end=' ')
    print()
