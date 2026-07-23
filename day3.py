# using different logics to check even or odd

# To check even or odd number
n=int(input('enter: '))
if n%2 == 0:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")


# To check even or odd number

n=int(input("enter: "))
if n%2 !=0:
    print(f"{n}is odd number")
else:
    print(f"{n}is even number")


# To check even or odd number

n=int(input("enter: "))
if n%2 == 1:
    print(f"{n}is odd number")
else:
    print(f"{n}is even number")


# To check even or odd number

n=int(input("enter: "))
if n%2 !=1:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")

# To check even or odd number

n=int(input("enter: "))
if (n//2)*2 == n:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")

# To check even or odd number

n=int(input("enter: "))
if (n//2)*2 != n:
    print(f"{n}is odd number")
else:
    print(f"{n}is even number")

# To check even or odd number

n=int(input("enter: "))
if n & 1 ==0:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")

# To check even or odd number

n=int(input("enter: "))
if n & 1 == 1:
    print(f"{n}is odd number")
else:
    print(f"{n}is even number")


# To check even or odd number

n=int(input("enter: "))
if n | 1 == n+1:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")


# To check even or odd number

n=int(input("enter: "))
if n | 1 == n:
    print(f"{n}is odd number")
else:
    print(f"{n}is even number")

# To check even or odd number

n=int(input("enter: "))
if n | 1 != n:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")

# To check even or odd number

n=int(input("enter: "))
if n | 1 != n:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")

# To check even or odd number

n=int(input("enter: "))
if n ^ 1 == n+1:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")


# To check even or odd number

n=int(input("enter: "))
if n ^ 1 == n-1:
    print(f"{n}is odd number")
else:
    print(f"{n}is even number")

# To check even or odd number

num = int(input("Enter a number: "))
match num % 2:
    case 0:
        print("Even")
    case 1:
        print("Odd")


# To check even or odd number
num = int(input("Enter a number: "))
if (~num & 1):
    print("Even")
else:
    print("Odd")


# To check even or odd number

n=int(input("enter: "))
l=['even','odd']
print(l[n%2])

# To check even or odd number

n=int(input("enter: "))
l=('even','odd')
print(l[n%2])

# To check even or odd number

n = int(input("Enter: "))
l = {0: "even", 1: "odd"}
print(l[n % 2])

# To check even or odd number

n=int(input("enter: "))
if (n>>1)<<1 == n:
    print(f"{n}is even number")
else:
    print(f"{n}is odd number")

# To check even or odd number

n=int(input("enter: "))
if (n>>1)<<1 != n:
    print(f"{n}is odd number")
else:
    print(f"{n}is even number")