#polymorphsm---------------------------
# poly is a many
# morphsm is a forms 

# 1. operator overloading
# 2. method overloading
# 3. method overriding

# 1. operator overloading =
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,otr):
#             return self.m1+self.m2,otr.m1+otr.m2
        
# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1+s2)

# #__sub__(substraction)=
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __sub__(self,otr):
#             return self.m1-self.m2,otr.m1-otr.m2
        
# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1-s2)

# #__mul__(multiplication)=

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __mul__(self,otr):
#             return self.m1*self.m2,otr.m1*otr.m2
        
# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1*s2)

# #__truediv__(division)=
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __truediv__(self,otr):
#             return self.m1/self.m2,otr.m1/otr.m2
        
# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1/s2)

# #__gt__(greaterthan)=
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __gt__(self,otr):
#             return self.m1>self.m2,otr.m1>otr.m2
        
# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1>s2)

# 2. method overloading=

# 3. method overriding
# class a:
#     def __init__(self):
#         pass
#     def hello(self):
#         print ("a hello")

# class b(a):
#     def __init__(self):
#         pass
#     def hello(self):
#         print ("b hello")
# b1 = b()
# b1.hello()




