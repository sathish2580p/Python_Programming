# l1=[]
# n =int(input('n:'))
# l1=[int(input('n: ')) for i in range(n)]
# print(l1)
# # output:
# # n:2
# # n: 4
# # n: 2
# # [4, 2]

# n=int(input('n: '))
# l1=eval(input()[:n])
# print(l1,type(l1))
# # output:
# # n: 2
# # 4
# # 4 <class 'int'>


# n=int(input('n: '))
# l1=[]
# for i in range(n):
#     val=input('val: ')
#     try:
#         l1.append(int(val))
#     except:
#         try:
#             l1.append(float(val))
#         except:
#             try:
#                 l1.append(complex(val))
#             except:
#                 l1.append(val)
# print(l1)
# # output:
# # n: 3
# # val: 2
# # val: don
# # val: 2.5
# # [2, 'don', 2.5]


# n=int(input('n: '))
# l1=list(map(int,input().split()))
# print(l1)
# # output:
# # n: 2
# # 4 5
# # [4, 5]

# n=int(input('n: '))
# l1=list(map(int,input().split()))[:n]
# print(l1)
# # output:
# # n: 2
# # 3 5
# # [3, 5]

# l1=[10,20,10,30,40,50,50]
# d={}
# for i in l1:
#     d[i]=l1.count(i)
# print(d)

# import collections as c
# l1=[10,20,10,30,40,50,50]
# print(c.Counter(l1))


# l1=[10,20,10,30,40,50]
# l2=[50,40,30,10,20,10]
# if l1==l2[::-1]:
#     print('palindrome')
# else:
#     print('not a plaindrome')


# l1=[10,20,10,30,40,50]
# count=0
# for i in l1:
#     count +=1
# print(count)


# l1=[10,20,10,30,40,50]
# l2=[5,2,10,20,47,97,87]
# res=list(set(l1).intersection(set(l2)))
# print(res)

# l1=[10,20,60,30,40,50]
# l2=[5,2,10,20,47,97,87]
# res=[]
# for i in l1:
#     if i in l2:
#         res.append(i)
# print(res)

# l1=[10,20,60,30,40,50]
# l2=[5,2,10,20,47,97,87]
# l=l1 if len(l1)<len(l2) else l2
# print(l)
# res=[]
# for i in l:
#     if i in l1 and i in l2:
#         res.append(i)
# print(res)

# l1=[10,20,60,30,40,50,50,60]
# l1.sort()
# l=set(l1)
# print(list(l1[-2]))


#------------------------------------------------------


# l1=['7','l','@','2','u','8','H','2','$','a','r','1','r']

# op=['r','1','@','r','a','2','H','8','$','u','2','l','7']

# print(l1)
# cnt=0
# for i in l1:
#   if i>='a' and i<='z' or i>='A' and i<='Z' or i>='0' and i<='9':
#     cnt+=1

# #create new list which accepts total number of values in cnt
# l2=[None]*cnt
# # print(l2)

# #store only numbers and chars to new list
# j=0
# for i in range(len(l1)):
#   if l1[i]>='a' and l1[i]<='z' or l1[i]>='A' and l1[i]<='Z' or l1[i]>='0' and l1[i]<='9':
#     l2[j]=l1[i]
#     j+=1
# #print(l2)
# #reverse the list

# l2=l2[::-1]
# # print(l2)

# #assign the l2 elements to l1 if  it is char or numbers
# j=0
# for i in range(len(l1)):
#   if l1[i]>='a' and l1[i]<='z' or l1[i]>='A' and l1[i]<='Z' or l1[i]>='0' and l1[i]<='9':
#     l1[i]=l2[j]
#     j+=1

# print(f'after replacing{l1}')


# l1=[2,12,18,27,35,46,58]
# l2=[]
# for i in range(l1[0],l1[-1]):
#   if i not in l1:
#     l2.append(i)
# print(l2)

# [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22,
#  23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 
#  41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

# l1=[1,2,3,11,45,12,11,40,65,5,7,9,11,34,57,10]
# target=11
# index_ls=[]
# for i in range(len(l1)):
#   if l1[i]==target:
#     index_ls=i
# if target in l1:
#    print(tuple([index_ls[0],index_ls[-1]]))
# else:
#    print((-1,-1))
  
# WAP to display pairs of given target  value

# l1=[2,1,5,6,7,8,4,3,2,5,8,9,1,2,4,5]
# target=6
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]+l1[j] == target:
#             print((l1[i],l1[j]))


# WAP  to display given list primes numbers sum

# def is_prime(n):
#    if n<=1:
#       return False
#    else:
#       for i in range(2,n):
#          if n%i==0:
#             return False
#       return True
# l1=[1,7,2,4,6,17,19,5,8,12,45,23,18,19,21]
# res=0
# for i in l1:
#    if is_prime(i):
#       res+=i
# print("sum of all primes :",res)


# l1=[1,2,3,4,5,6,7,8,9,10]
# o/p:[10,9,8,7,6,1,2,3,4,5]


# l1=[1,2,3,4,5,6,7,8,9,10]
# mid=len(l1)//2
# print(l1[mid:][::-1]+l1[:mid])


# WAP to display the nth largest value from the given list

# l1=[2,13,7,61,1,25,70,24,19,45]
# n=3
# l1.sort()
# if n<len(l1):
#    print((l1)[-n]) 
# else:
#    print(-1)
   
# def nth_largest(l1, n):
#    if len(l1) == 0:
#       return "list is empty"
#    elif n <= 0 or n > len(l1):
#       return -1
#    l2 = l1

#    for i in range(n):
#       max_val = l2[0]
#       idx=0

#       for j in range(1, len(l1)):
#          if l2[j] > max_val:
#             max_val = l2[j]
#             idx=j

#       if i == n-1:
#          return max_val
#       del l1[idx]

# l1=[2,13,7,61,1,25,70,24,19,45]
# n=5
# print(nth_largest(l1,n))




# l1=[[1,3],[4,5,6],[7,8,9,34],[2,67],[],[1,10],[2,3]]
# cnt=0
# for i in l1:
#     for j in i:
#         cnt +=1
# print(cnt)

# WAP to display max elemnets in each list

# l1=[[1,3],[4,5,6],[7,8,9,34],[2,67],[1,10],[2,3]]
# for i in l1:
#    if len(i) == 0:
#       continue
#    print(max(i),end=' ')


# l1=[[1,3],[4,5,6],[7,8,9,34],[2,67],[],[1,10],[2,3]]
# for i in l1:
#    if len(i) == 0:
#       continue
#    max_val = i[0]
#    for j in i:
#       if j > max_val:
#          max_val = j
#    print(max_val)
   

# WAP to display sum of column elements

# l1=[[1,3,2,4],
#     [4,5,6,8],
#     [7,8,9,34],
#     [2,67,1,10]]
# target=3
# res=0
# for i in l1:
#      if 0<target<len(i):
#       print(i[target-1],end=' ')
#       res+=i[target-1]
# print()
# print(res)


# WAP to build index grid system based on row and column using user input

# row=int(input('enter: '))
# col=int(input('enter: '))
# outer=[]
# for i in range(row):
#    inner=[]
#    for j in range(col):
#       inner += [(i,j)]
#    outer += [inner]
# print(outer)


# row=int(input('enter: '))
# col=int(input('enter: '))
# print([[(i,j) for j in range(col)] for i in range(row)])

# WAP to accept the values from the user to the given matrix and dispaly it in the form of matrix

# row=int(input('enter: '))
# col=int(input('enter: '))
# matrix1 = [[int(input()) for j in range(col)] for i in range(row)]
# print(matrix1)
# for i in matrix1:
#    for j in i:
#       print(j,end=' ')
#    # print()


# row=int(input('enter: '))
# col=int(input('enter: '))
# matrix1 = [[int(input()) for j in range(col)] for i in range(row)]
# print("matrix1")
# for i in matrix1:
#    for j in i:
#       print(j,end=' ')
#    print()
# print()
# matrix2 = [[int(input()) for j in range(col)] for i in range(row)]
# print("matrix2")
# for i in matrix2:
#    for j in i:
#       print(j,end=' ')
#    print()

# result = [[0 for j in range(col)] for i in range(row)]

# for i in  range(len(matrix1)):
#    for j in range(len(matrix2)):
#       result[i][j]=matrix1[i][j] + matrix2[i][j]
# print()
# print("result")



# row=int(input('enter: '))
# col=int(input('enter: '))
# matrix1 = [[int(input()) for j in range(col)] for i in range(row)]
# print("matrix1")
# for i in matrix1:
#    for j in i:
#       print(j,end=' ')
#    print()
# print()
# matrix2 = [[int(input()) for j in range(col)] for i in range(row)]
# print("matrix2")
# for i in matrix2:
#    for j in i:
#       print(j,end=' ')
#    print()

# result = [[0 for j in range(col)] for i in range(row)]

# # matrix multiplication

# for i in  range(len(matrix1)):
#    for j in range(len(matrix2[0])):
#       for k in range(len(matrix2)):
#          result[i][j] += matrix1[i][k] * matrix2[k][j]


# print()
# print('result')
# for i in result:
#    for j in i:
#       print(j,end=' ')
#    print()

# WAp find the difference of sum of primary and seccondary diagonal elements

# row=int(input('enter: '))
# col=int(input('enter: '))
# matrix1 = [[int(input()) for j in range(col)] for i in range(row)]
# print("matrix1")
# for i in matrix1:
#    for j in i:
#       print(j,end=' ')
#    print()
# print()
# matrix2 = [[int(input()) for j in range(col)] for i in range(row)]
# print("matrix2")
# for i in matrix2:
#    for j in i:
#       print(j,end=' ')
#    print()

# result = [[0 for j in range(col)] for i in range(row)]

# # matrix multiplication

# for i in  range(len(matrix1)):
#    for j in range(len(matrix2[0])):
#       for k in range(len(matrix2)):
#          result[i][j] += matrix1[i][k] * matrix2[k][j]


# print()
# print('result')
# for i in result:
#    for j in i:
#       print(j,end=' ')
#    print()


# row=int(input('enter: '))
# col=int(input('enter: '))


# matrix2 = [[int(input()) for j in range(col)] for i in range(row)]

# print("matrix2")
# for i in matrix2:
#    for j in i:
#       print(j,end=' ')
#    print()

# pd=0
# sd=0
# for i in range(row):
#     for j in range(col):
#         if i==j:
#            pd+=matrix2[i][j]
#         if i+j==row-1:
#            sd+=matrix2[i][j]


# print(pd,sd)
           


# l1=[1,2,3,1,4,5,1,3,4,1,4,5,1,1,5,6,1,4,5,1,4,6,6]
# l2=[1,4,5]
# cnt=0
# for i in range(len(l1)):
#     if l1[i: i+len(l2)]==l2:
#         cnt +=1

# print("l2 is present for :",cnt,'times in l1')

#WAP to count vowels and consonents without spaces

# s1='python programming is Awesome'
# print(len(s1))
# v=0
# c=0
# for i in s1:
#     if i == ' ':
#         continue
#     elif i in 'aeiouAEIOU':
#         v +=1
#     else:
#         c +=1
# print('vowels :',v)
# print('consonents :',c)


# WAP to change uppercase to lowercase and lowercase to  uppercase without using swap method
        
# s1='python programming is Awesome'
# s2=''
# for i in s1:
#     if i >= 'a' and i<= 'z':
#         s2 += chr(ord(i) - 32)
#     elif i>= 'A' and i <= 'Z':
#         s2 += chr(ord(i) +32)
#     else:
#         s2 +=i

# print(s2)



# WAP to convert snakecase character to camelcase

# s1='learning_python_programming_is_intersting'
# o/p: Learing Python Programming Is Intersting


# s1='learning_python_programming_is_intersting'
# s2=s1.split('_')
# print(s2)
# s3= ''
# for i in s2:
#     s3 += i.title() + ' '
# print(s3)


# s1='learning_python_programming_is_intersting'
# print(s1)
# s2= ''
# s2 += chr(ord(s1[0]) - 32)
# for i in range(1,len(s1)):
#     if s1[i] == '_':
#         s2 += ' '
#     elif s1[i-1] == '_':
#         s2 += chr(ord(s1[i]) -32)
#     else:
#         s2 += s1[i]
# print(s2)


# WAP to find the frequency of each character in the given string

# s1='python is a dynamically typed language'
# d1= {}
# for i in s1:
#     if i  not in d1:
#         d1[i] = 1
#     else:
#         d1[i] += 1
# print(d1)

# WAP to 
# s1= 'abcd'
# s2= 'wxyz'
# o/p:azbycxdw


# s1= 'abcd'
# s2= 'wxyz'
# j = len(s2) - 1 
# s3= ''
# for i in range(len(s1)):
#     s3 += s1[i] + s2 [j]
#     j -= 1
# print(s3)


# s1= 'abcd'
# s2= 'wxyz'
# s3= ''

# for i in range(len(s1)):
#     s3 += s1[i] + s2[len(s2)-1-i]

# print(s3)


# WAP count the total no.of special characters in each word of a given strin, if the count is even reverse that word in the same position

# s1= 'I@#$ am#$!@$% pool!@# Deadpool!@#$%& here!@# to!@#$%^&! kill!@#$ Bad!@# Guys!@#$'

# o/p: I@#$ %$@!#ma pool!@# &%$#@!loopdead here!@$ !&^%$#@!ot $#@!llik Bad!@# $#@!syuG

# s1= 'I@#$ am#$!@$% pool!@# Deadpool!@#$%& here!@# to!@#$%^&! kill!@#$ Bad!@# Guys!@#$'
# s2=s1.split(' ')
# print(s2)

# for i in s2:
#     cnt = 0
#     for j in i:
#         if j <= 'a' and j>= 'z' or j >= 'A' and j <= 'Z':
#             continue
#         else:
#             cnt +=1
#     print(i,'->',cnt) 
# if cnt%2==0:
#     s2.reverse
# print()



# program to check the given input string can became a password or not 
# it should contain one uppercase, one lowercase, one numeric, one special character and it should be the minimum lenght of 8 to 30 characters 
# input be like: Password@123

# def password_checker(s1):
#     uc,lc,nc,sc = 0,0,0,0
#     if len(s1) >= 8 and len(s1) <= 30:
#         for i in s1:
#             if i >='A' and i <= 'Z':
#                 uc += 1
#             elif i >= 'a' and i <='z':
#                 lc += 1
#             elif i >'0' and i <= '9':
#                 nc += 1
#             else:
#                 sc += 1
#         if uc >= 1 and lc >= 1 and nc >= 1 and sc >= 1:
#             print('valid password')
#         else:
#             print('invalid password')

#     else:
#         print('paswword should be min of 8 characters')


# s1=input('enter the password: ')
# password_checker(s1)



# s1='madam'

# j = len(s1)-1
# for i in range(len(s1)):
#     if s1[i] != s1[j]:
#         print('not pallindrome')
#         break
#     j -= 1
# else:
#     print('pallindrome')
    

# WAP to check given string mirror characters or not

# def mirror_str(s1):
#     chars = {'A','H','I','M','O','T','U','V','W','X','Y','o','v','w','x','0','8'}

#     for i in  s1:
#         if i  not in chars:
#             return False
#     return s1 == s1[::-1]

# if mirror_str('OYO'):
#     print('mirror char string')
# else:
#     print('not a mirror char string')



# program to convert the given string into encryption format based on  the given condition
# if char ascci value is even add extra +5 if it odd add +3 to it and convert to strings again



# s1='python'
# str=''
# for i in s1:
#     if ord(i) % 2 == 0:
#         str += chr(ord(i)+5)
#     else:
#         str += chr(ord(i)+3)
# print(f'encryption of string: {str}')


# after converting to the next ascii value check the char is present b/n the boundary,
#  if it is reaching out of the boundary bring back to the respective (assignment)


# WAP to display the index  values of unique word in the form of list along with the word as a key

# s1='if you always do what you always did you will always get what you always got'
# if :[0]
# you  :[1,5,8,13]
# always :[2,6,10,14]


# s1='if you always do what you always did you will always get what you always got'
# s2=s1.split()
# d1={}

# for i in range(len(s2)):
#     if s2[i] not in d1:
#         d1[s2[i]] = [i]
#     else:
#         d1[s2[i]] += [i]
# print(d1)
        

# s1='education is more powerful weapon in the world'
# education : [5,3]
# is : [1,1]
# more : [2,2]
# powerful : [3,5]

# s1='education is more powerful weapon in the world'
# d1= {}

# for i in s1.split():
#     vol=0
#     con=0
#     for j in i:
#         if j in 'AEIOUaeiou':
#             vol += 1
#         else:
#             con += 1
#     d1[i] = [vol,con]

# print(d1)


s1='the sky is blue'
s2=s1.split()
for i in range(len(s2)-1,-1,-1):
    print(s2[i],end=' ')

