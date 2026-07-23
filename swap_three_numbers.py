# swaping  three values using different logics

# using basic method 3rd variable
a=int(input("enter a: "))
b=int(input("enter b: "))      # input values
c=int(input("enter c: "))
print(f"a:{a}\tb:{b}\tc:{c}")  # display
d=a
a=c                            # logic to swap
c=b
b=d
print(f"a:{a}\tb:{b}\tc:{c}")  # display

# using arathamatic operations (+,-)

a=int(input("enter a: "))
b=int(input("enter b: "))      # input values
c=int(input("enter c: "))
print(f"a:{a}\tb:{b}\tc:{c}")  # display
a=a+b+c
b=a-(b+c)                      # logic to swap
c=a-(b+c)
a=a-(b+c)
print(f"a:{a}\tb:{b}\tc:{c}")  # display


# using  arathamatic operations (*,//)

a=int(input("enter a: "))
b=int(input("enter b: "))      # input values
c=int(input("enter c: "))
print(f"a:{a}\tb:{b}\tc:{c}")  # display
a=a*b*c
b=a//(b*c)                      # logic to swap
c=a/(b*c)
a=a//(b*c)          # zero division error whwn we use 0
print(f"a:{a}\tb:{b}\tc:{c}")  # display


# using XOR logic

a=int(input("enter a: "))
b=int(input("enter b: "))      # input values
c=int(input("enter c: "))
print(f"a:{a}\tb:{b}\tc:{c}")  # display
a=a^b^c
b=a^b^c                        # logic to swap
c=a^b^c
a=a^b^c
print(f"a:{a}\tb:{b}\tc:{c}")  # display


# using ab,c=c,a,b(packing and unpacking)

a=int(input("enter a: "))
b=int(input("enter b: "))      # input values
c=int(input("enter c: "))
print(f"a:{a}\tb:{b}\tc:{c}")  # display
a,b,c=c,a,b                    # logic to swap
print(f"a:{a}\tb:{b}\tc:{c}")  # display

