# swap two numbers using different logics

# using basic method temp variable

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
temp=a                      # logic
a=b
b=temp
print(f'a:{a}\tb:{b}')      # to display 

# without using basic method temp variable using arathamatic operators

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
a=a+b                       # logic
b=a-b
a=a-b
print(f'a:{a}\tb:{b}')      # to display 

# uisng multiplication and floor division

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
a=a*b                       # logic
b=a//b                      # ( in this case one draw back is there zero divion error will occur)
a=a//b
print(f'a:{a}\tb:{b}')      # to display 

# using bitwise operator

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
a=a^b                       # logic
b=a^b
a=a^b
print(f'a:{a}\tb:{b}')      # to display 

# using (a,b=b,a)  tuple unpacking  method

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
a,b=b,a                     # logic
print(f'a:{a}\tb:{b}')      # to display 

# using (a,b=b,a)  List unpacking  method

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
[a,b]=[b,a]                 # logic
print(f'a:{a}\tb:{b}')      # to display 

# using dictionary method

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
d = {"a": b, "b": a}        # logic
a = d["a"]
b = d["b"]
print(f'a:{a}\tb:{b}')      # to display 

# using function method

def swap(x, y):
    return y, x
a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
a,b= swap(a,b)
print(f'a:{a}\tb:{b}')      # to display

# using List method

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
l = [a,b]                  # logic
a = l[1]
b = l[0]
print(f'a:{a}\tb:{b}')      # to display 

# using Lambda function

a=int(input('enter a: '))   # user input a
b=int(input('enter b: '))   # user input b
print(f'a:{a}\tb:{b}')      # to display
swap = lambda x, y: (y, x)  # logic
a, b = swap(a, b)
print(f'a:{a}\tb:{b}')      # to display 

# using class method

class Swap:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def swapping(self):
        self.a, self.b = self.b, self.a
obj = Swap(10, 20)
print(obj.a, obj.b)
obj.swapping()
print(obj.a, obj.b)
