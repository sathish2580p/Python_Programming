# n=int(input('n: '))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n=int(input())
# print(n*(n+1)//2)

# n=int(input())
# print(n*(n+1)*(2*n+1)//6)

# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i**2
# print(sum)

# n=int(input())
# print(n*(n+1)*(2*n+1)//6)


# n=int(input())
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# n=int(input())
# sum=0
# for i in range(1,n+1,2):
#     sum+=i
# print(sum)


# n=int(input())
# print((n//2)*(n//2+1))


# n=int(input())
# res=1
# for i in range(1,n+1):
#     res*=i
# print(res)

# n=int(input())
# for i in range(1,n+1):
#     if n % i ==0:
#         print(i,end=' ')

# n=int(input())
# res=0
# while n>0:
#     ld=n%10
#     if ld%2==0:
#         res+=ld
#     n=n//10
# print(res)

# counting the factors of a number
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# print(c)
#o/p:
#100
# 9

# n=int(input())
# c=0

# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print(f'{n} is a prime number')
# else:
#     print(f'{n} is not a prime number')


# n=int(input())
# c=0
# lc=0
# for i in range(2,n//2+1):
#     if n%i==0:
#         lc=0
#         c+=1
#         break
# if c==0:
#     print(f'{n} is a prime number')
# else:
#     print(f'{n} is not a prime number')
# print(lc)


# n=int(input())
# c=0
# for i in range(2,n//2+1):
#     if n%i==0:
#         c+=1
#         break
# if c==0:
#     print(f'{n} is a prime number')
# else:
#     print(f'{n} is not a prime number')

# from math import *
# n=int(input())
# c=0
# for i in range(2,int(sqrt(n))+1):
#     if n%i==0:
#         c+=1
#         break
# if c==0:
#     print(f'{n} is a prime number')
# else:
#     print(f'{n} is not a prime number')

# from math import *
# n=int(input('n: '))
# c=0
# lc=0
# for i in range(2,int(sqrt(n))+1):
#     lc+=1
#     if n%i==0:
#         c+=1
#         print(f'{n} is not a prime number')
#         break
# else:
#     print(f'{n} is a prime number')
# print(lc)

# n=int(input('n: '))
# res=0
# while n>0:
#     res+=n%10
#     n//=10
# print(res)


# n=int(input('n: '))
# res=0
# for i in str(n):
#     res+=int(i)
# print(res)


# n=int(input('n: '))
# res=sum([int(x) for x in str(n)])
# print(res)

# n=int(input('n: '))
# print(sum([int(x) for x in str(n)]))


# n=int(input('n: '))
# print(sum([int(x) for x in str(n) if int(x)%2==0]))
