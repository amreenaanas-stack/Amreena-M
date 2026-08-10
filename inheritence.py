# inheritence-------------------------------------------
# 1. single line 
# 2. multi line 
# 3. multiple line 

# parent class
#     child class 



#1. single line=
# class person1:

#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def smile(self):
#         print("person can smile hahaha")
#     def speak(self):
#         print("person 1 can speak hahaha")

# class person2(person1):

#     def __init__(self):
#         pass
#     def read (self):
#         print("person can read")
#     def write (self):
#         print("person can write")
#     def speak(self):
#         print("person 2 can speak hahaha")    

# p1 = person1()
# p1.walk()
# p1.smile()
# p2 = person2()
# p2.read()
# p2.write()

# # 2. multi line =

# class person3(person2):

#     def __init__(self):
#         pass
#     def fly(self):
#         print("person can fly")
#     def swim(self):
#         print("person can swim")
#     def speak(self):
#         print("person 3 can speak hahaha")

# class person4(person3):

#     def __init__(self):
#         pass
#     def sleep (self):
#         print("person can sleep")
#     def eat (self):
#         print("person can eat")
#     def speak(self):
#         print("person 4 can speak hahaha")    
#         super().speak()
# p4 = person4()
# p4.speak()


# 3. multiple line =

class person1:

    def __init__(self):
        pass
    def walk(self):
        print("person can walk")
    def smile(self):
        print("person can smile hahaha")
    def speak(self):
        print("person 1 can speak hahaha")

class person2:

    def __init__(self):
        pass
    def read (self):
        print("person can read")
    def write (self):
        print("person can write")
    def speak(self):
        print("person 2 can speak hahaha")

class person3:

    def __init__(self):
        pass
    def fly(self):
        print("person can fly")
    def swim(self):
        print("person can swim")
    def speak(self):
        print("person 3 can speak hahaha")

class person4(person3,person2,person1):

    def __init__(self):
        pass
    def sleep (self):
        print("person can sleep")
    def eat (self):
        print("person can eat")
    def speak(self):
        print("person 4 can speak hahaha")    
        super().speak()
p4 = person4()
p4.speak()

                     






