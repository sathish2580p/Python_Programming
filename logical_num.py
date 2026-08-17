# reverse the entered number
n= int(input('n: '))
print(str(n)[::-1])
#output
# n: 123
# 321

# reverse the entered number
n=int(input('n: '))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)
# output
# n: 123
# 321

# check enter number is palindrome or not
n=int(input('n: '))
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if rev==temp:
    print('palindrome')
else:
    print('not a palindrome')
# output
# n: 323
# palindrome

# check enter number is palindrome or not
n=int(input('n: '))
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if str(n)==str(n)[::-1]:
    print('palindrome')
else:
    print('not a palindrome')
# output
# n: 323
# palindrome

# # check given number is amstrong number

n= int(input('n: '))
res= 0
temp=n
p=len(str(n))
while n>0:
    rem=n%10
    res+=rem**p
    n//=10
if temp==res:
    print('amstrong number')
else:
    print('not a amstrong number')
# output
# n: 153
# amstrong number


# entered number strong number or not
n= int(input('n: '))
res= 0
temp=n
while n>0:
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact*=1
    res+=fact
    n//=10
if temp==res:
    print('strong number')
else:
    print('not a strong number')
# output
# n: 123
# not a strong number

# perfect number
n= int(input('n: '))
res=0
for i in range(1,n//2+1):
    if n%i==0:
        res+=i
if res==n:
    print('perfect number')
else:
    print('not a perfect number')
# output
# n: 6
# perfect number

# harshads number
n= int(input('n: '))
temp=n
res=0
while n>0:
    res+=n%10
    n//=10
if temp%res==0:
    print('harshads number')
else:
    print('not a harshads number')
# output
# n: 70
# harshads number

# automorphic number
n= int(input('n: '))
res=n**2
if n==int(str(res)[-len(str(n)):]):
    print('automorphic number')
else:
    print('not automorphic number')
# output
# n: 6
# automarphic number

# neon number
n= int(input('n: '))
res=n**2
sum=0
while res>0:
    sum+=res%10
    res//=10
if sum==n:
    print('neon number')
else:
    print('not a neon number')
# output
# n: 9
# neon number
