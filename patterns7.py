n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
# * * * * * 
# * *   * * 
# *   *   * 
# * *   * * 
# * * * * * 

n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if j==0 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
# *         
# *         
# * * * * * 
# *         
# *   

n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
#         * 
#         * 
# * * * * * 
#         * 
#         * 
n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
#     *     
#     *     
#     *     
#     *     
# * * * * * 
n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
# *       * 
#   *   *   
#     *     
#   *   *   
# *       * 
n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or i==n-1 or (j==0 and i<n//2) or (j==n-1 and i>n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
# * * * * * 
# *         
# * * * * * 
#         * 
# * * * * * 


n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i+j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
# * * * * * 
# *       * 
# *   *   * 
# *       * 
# * * * * * 
n=int(input('n: '))
for i in range(n):
    for j in range(n):
        if (j==0 and i==0) or (i==n-1 and j==n-1) or (i==n-1 and j==0) or (j==n-1 and i==0):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
#output
# n: 5
#   * * *   
# * * * * * 
# * * * * * 
# * * * * * 
#   * * *  

n=int(input('n: '))
for i in range(n):
    for j in range(n*2-1):
        if (i==n-1) or (i+j==n-1) or (j-i==(n-1)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
#         *         
#       *   *       
#     *       *     
#   *           *   
# * * * * * * * * * 
n=int(input('n: '))
for i in range(n):
    for j in range(2*n-1):
        if i==0 or i+j==(2*n-2) or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
# n: 5
# * * * * * * * * * 
#   *           *   
#     *       *     
#       *   *       
#         *    
n=int(input('n: '))
val=3
for k in range(val):

    for i in range(n):
        for j in range(2*n-1):
            if i==n-1 or i+j==(n-1) or j-i==n-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
#output
# n: 5
#         *         
#       *   *       
#     *       *     
#   *           *   
# * * * * * * * * * 
#         *         
#       *   *       
#     *       *     
#   *           *   
# * * * * * * * * * 
#         *         
#       *   *       
#     *       *     
#   *           *   
# * * * * * * * * * 