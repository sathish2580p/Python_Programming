# #sum of list elements
# # input:
# # 5
# # 10 3 4 5 7
# # output:
# # 29

# n=int(input('n: '))
# l1=list(map(int,input().split()))
# res=0
# for i in l1:
#     res+=i
# print(res)
# # output:
# # n: 3
# # 2 4 7
# # 13

# #sum of list elements
# # input:
# # 5
# # [10,3,3.4,don,khan]
# # output:
# # 16.4

# n=int(input('n: '))
# l1=eval(input())[:n]
# res=0
# for i in l1:
#     if type(i) in [int,float,complex]:    # is int and i==int like that also we can use
#         res+=i
# print(res)
# # output:
# # n: 5
# # [10,3,3.4,'don','khan']
# # 16.4

# n=int(input('n: '))
# l1=eval(input())[:n]
# res=0
# for i in l1:
#     if isinstance(i,(int,float,complex)):
#         res+=i
# print(res)
# # output:
# # n: 3
# # [2,3,4]
# # 9



# l=[1,2,3,4,5,6]
# ec,oc=0,0
# for i in l:
#     if i%2==0 and i !=0:
#         ec+=1
#     elif i!= 0 and i%2 !=0:
#         oc+=1
# print(ec,oc,sep='\n')

# l=[1,2,3,4,5,6]
# ec,oc=0,0
# for i in l:
#     if i%2==0 and i !=0:
#         ec+=i
#     elif i!= 0 and i%2 !=0:
#         oc+=i
# print(ec,oc,sep='\n')


# l1=[1,52,3,46,65,6,22]
# max=l1[0]
# for i in l1:
#     if i>max:
#         max=i
# print(max)


# l1=[1,52,3,46,65,6,22]
# min=l1[0]
# for i in l1:
#     if i<min:
#         min=i
# print(min)

# l1=[1,52,3,46,65,6,22]
# print(l1)
# res=l1[::-1]
# print(res)
 
# l1=[1,52,3,46,65,6,22]
# print(l1)
# i,j=0,len(l1)-1
# while i<j:
#     l1[i],l1[j]=l1[j],l1[i]
#     i+=1
#     j-=i
# print(l1)

print(ord('9'))