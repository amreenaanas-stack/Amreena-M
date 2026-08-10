#functions is a blocks of code---------------------------------
#WHICH IS EXECUTED WHEN IT IS CALLED
#USING:STRUCTURAL,FUNCTIONAL,PROCEDUAREL PROGRAMIN
#FUNCTION CODE:
# def funcionname(<arguments kodukkuka>):
#     code to be executed 

#EG:
# def hello():
#     print("hello good afternoon!!!")
# hello() #CALLING FUNCION

#another example 
    
# def saymyname():
#     print("my name is amreena")
# saymyname()

#ARGUMENTS--------------------------------------
#values to passed to a function
# def add2(a,b): #former parameter:
#     print(a+b)
# add2(1,2) #actual parameter:



#types of arguments-------------------------------

#1.positional arguments=
# def add2(a,b):
#     print(a+b)
# add2(3,5)    

# #2. keyword argument=
# def fullname(fname,mname,lname):
#     print(fname+' '+mname+' '+lname)
# fullname(fname="di" , mname="ls", lname="sha")   

# #default argument
# def aa2(a=0,b=0):
#     print(a+b)
# aa2(3,4)
# aa2()    
#return statement

# lambda function----------------------------------------------------
# anonymous fuction

# lambda argumenets : expression

# def add2(a,b):
#     return a+b
# print(add2(1,4))

## product of 3 numbers
# a= lambda x,y,z : x*y*z
# print(a(4,3,2))
# square of a number
# perimeter of a circle
# area of a triangle
# square root of a number
# full name of a person

# z= lambda x,y :x+y
# print(z(2,3))

# product of 3 numbers
# z= lambda a,b,c : a*b*c
# print(z(4,3,5))

# square of a number
# z=lambda x,y :x**y
# print(z(2,3))

# perimeter of a circle
# z=lambda r : 2*3.14*r
# print(z(6))

# area of a triangle
# z=lambda r:3.14*r**r
# print(z(3))

# square root of a number
# z=lambda x: x**0.5
# print(z(2))

# full name of a person
# z=lambda fname,lname:fname+" "+lname
# print(z("Dilsha","musthafa"))

#eligibility checking
# check= lambda age:"eligible" if age>=18 else "not eligible"
# print(check(19))

#age
# a=lambda current,born:current-born
# print(a(2026,2005))

