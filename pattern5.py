n=int(input('enter: '))
spc=n-1
str=1
for i in range(n):
    for j in range(spc):
        print(' ', end=' ')
    for k in range(str):
        print('*', end=' ') 
    print()
    spc-=1
    str+=2
#output:
# enter: 5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

n=int(input('enter: '))
str=1
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(str):
        print('*', end=' ') 
    print()
    str+=2
#output:
# enter: 5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

n=int(input('enter: '))
for i in range(n):
    for j in range(n-1-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ') 
    print()
#output:
# enter: 5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

n=int(input('enter: '))
for i in range(n):
    print('  '*(n-1-i)+'* '*(2*i+1))

#output:
# enter: 5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

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

n=int(input('enter: '))
val=1
for i in range(n):
    print('  '*(i)+(str(val)+' ')*(2*(n-i)-1))
    val+=1
#output:
# enter: 5
# 1 1 1 1 1 1 1 1 1 
#   2 2 2 2 2 2 2 
#     3 3 3 3 3 
#       4 4 4 
#         5 

n=int(input('enter: '))
for i in range(n-1,-n,-1):
    for j in range(n-abs(i)):
        print('*',end=' ')
    print()

#output:
# enter: 5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n=int(input('enter: '))
for i in range(n-1,-n,-1):
    print('* '*(n-abs(i)))
print()

n=int(input('enter: '))
for i in range(n-1,-n,-1):
    print(' '*abs(i) +'  * '*(n-abs(i)))
print()

#output:
# enter: 5
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

n=int(input('enter: '))
for i in range(n-1,-n,-1):
    print('  '*abs(i) +'* '*(n-abs(i)))
print()

#output:
# enter: 5
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

