#list comrehension-----------------------------------

# a = []
# for i in range(1,101):
#     a.append(i)
# print(a)

# a = [i for i in  range(1,101) if i % 2 == 0 ]
# print(a)


#question ?
#create a list wuth numbers that are multiples of 3 and 5
# create a list of first 1000 numbers that has digit 6 in them
# eg[6,16,26,36,46,56,60,61,62....600...,656...996]

#answer=
# num = [i for i in range (1,101) if i%5==0 and 1%3=0]
# n6 = [i for in range(1,1001) if "6" in str(1)]
# print(n6)


#regular expression

import re 
#pattern = r"\d{4}-\d{4}-\d{4}-\d{4}-\d{4}"
Pattern= r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}"
data= "my adar number is 123-12345-12345-2346"
# \d -- oru decimal digit
# \w - alpha numeric
# \d
print(re.search(Pattern,data))

import re
# pattern=r"[a-z][A-Za-z0-9!#$%^&*()_+]+@[a-z]+.[a-z]+"  #[]+ --- for repeatation
# data=" my email is diSHa132567##$56&*^%$@gmail.com"
# print(re.search(pattern,data))



# import re
# pattern=r"([a-z][A-Za-z0-9!#$%^&*()_+]+)@([a-z]+).([a-z]+)"  #[]+ --- for repeatation
# data=" my email is diSHa132567##$56&*^%$@gmail.com, sJTMBGl34638$&*@gmail.com, dgjIKSGYD3258494#$^*@gmail.com"
# #z=re.findall(pattern,data)
# z=re.search(pattern,data)
# #1print(z)
# print(z.group(3))
# # for i in z:
# #     print(i)










