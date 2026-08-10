# # find vowels and their position in a string-----------------------
## a="hari"
#  'a' at location 1
# # 'i' at location 3
# # eg for laptop
# for i in range(len(a)):
#             if a[i] in "aeiou":
#               print(f"'{a[i]}' at location {i}")

# # b="amby"
# # for i in range(len(b)):
# #     if b[i] in "aeiou":
# #         print(f"'{b[i]}' at location {i}")

# #  c="amreena"
#  # for i in range(len(c)):
# #     if c[i] in "aeiou":
# #         print(f"'{c[i]}' at location {i}")

# # #example:(real easy way)
# # name=input("enter name:-")
# # for i in range(0, len(name)):
# #     if name[i] =="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u":
# #         print(i,name[i])

# #  #another easy way
# # name=input("enter name:-") 
# #    #vowek="aeiou"  
# # for i in range(0, len(name)):
# #     if name[i] in "aeiou":
# #         print(i,name[i]) 

# #Create a list of even numbers and odd numbers from first 100 numbers 

# # num=[]
# # even=[]
# # odd=[]
# # for i in range(1, 101):
# #  #print(i)
# #     num.append(i)
# #  #print(num)
# # for i in num:
# #     if i%2==0:
# #         even.append(i)
# #     else:
# #         odd.append(i)
# # print(even)
# # print(odd)
  

# # #remove duplicate from a list
# # c=[1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
# # b=[]
# # for i in c:
# #     if i not in b:
# #         b.append(i)
# # print(b)


# #break cntinue pass----------------------------------
# # .pass
# # .Loop
# # .break
# # .continue

# #if age >=18:
# pass
# #b=10
# #print(b)

# #while 1< 5:
# #pass

# # for i in range(1,11):
# #     if i ==6:
# #      continue 
# #     print(i)

# # for i in range (1,11):
# #     if i == 6:
# #        break
# #     print(i)


# # num=int(input('enter your number:--'))
# # if num == 1:
# #        print("not prime")
# # else:
# #     for i in range (2,num):
# #         if num % i == 0:
# #          print("not a prime number ")
# #          break
# #     else:
# #        print("prime number")


# #input n words make it into a sentence ?
# reverse of a string without using[::-1] 

#ith oru question thannathan sir 
# a=[11,13,14,15,16,17,18,19,20,12]

# mid = len(a)//2
# c=[]
# d=[]
# for i in range(len(a)):
#     if i < mid:
#         c.append(a[i])
#     else:
#         d.append(a[i])
# print(c)
# print(d)



# a=[11,1,100,-900,15,16]
# # print largest and smallest int from this list
# largest = 0
# smallest = 0
# for i in a:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print(largest,smallest)

#print i j using star(*)-------------
# i=rows
# j=c0lumns
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or i == 5 or j == 3:
#             print("*",end="")
#         else:
             
#              print( " ",end="")
#     print()
   