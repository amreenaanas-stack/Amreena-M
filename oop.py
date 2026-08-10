#object oriented programing-----------------------
# object?
# its a real worls entity
#0bject is an instence of an class

# 2=
# attributes=define an object
# behaviours/methods

# 3=class
# it is a blue print of an object(to create objects)
# eg=
# carnte attribute=colour,model,price
# code=car red aanenn parayan
# (color="red")
#methods is a funvtion(behaviour) inside a class

# class car:
#     def start():
#         print("car has started")
#     def stop():
#         print("car has stopped")
# c1 = car
# c2 = car
# c3 = car
# c3 = car
# c2.start()
# c2.stop()

# class bike:
#     def start():
#         print("bike has started")
#     def stop():
#         print("bike has stopped")
# b1 = bike
# b2 = bike
# b3 = bike
# b3 = bike
# b2.start()
# b2.stop()

#constructor----------------------------------------------
# __init__
# used to initialize an object
#this
# class car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c 
#         #print("object oriented")
#     def start(self):
#         print(f"{self.name} has started")
#     def stop(self):
#         print("car has stopped")
# c1 = car("swift","black")
# c2 = car("BMW","red")
# c3 = car
# c3 = car
# c2.start()
# c2.stop()

#create a class student ?
# with 6 attributes name m1 , m2 , n3 , m4 , m5
# 3 methods
# sum of marks()
# average of marks()
# display()
# class student():
#     def __init__(self,n,m1,m2,m3,m4,m5):
#      self.name=n
#      self.mark1=m1
#      self.mark2=m2
#      self.mark3=m3
#      self.mark4=m4
#      self.mark5=m5
#     def start(self):
#         print(self.name)
#         print(f"sum={self.mark1+self.mark2+self.mark3+self.mark4+self.mark5}")  
#     def stop(self):
#         print(f"avg={(self.mark1+self.mark2+self.mark3+self.mark4+self.mark5)/5}")  
# s1=student("amreena",50,50,50,50,50)
# s2=student("dilsha",49,49,49,49,49)
# s1.start()
# s1.stop()

#or

# class student():
#     def __init__(self,n,m1,m2,m3,m4,m5):
#      self.name=n
#      self.m1=m1
#      self.m2=m2
#      self.m3=m3
#      self.m4=m4
#      self.m5=m5
#     def sum_of_marks(self):
#         return self.m1+self.m2+self.m3+self.m4+self.m5
#     def average_of_marks(self):
#         return self.sum_of_marks()/5
#     def display(self):
#         print(f"student {self.name}has marks of{self.m1},{self.m2},{self.m3},{self.m4},{self.m5},the sum of marks is {self.sum_of_marks()} and the average of mark is {self.average_of_marks()}")
# s1 = student("amby",45,46,47,48,49)
# s1.display()

# quiz game with timer-------------------------------------
# import time 

# def quiz_game():
#     questions = [
#         ("What is the capital of France?", "Paris"),
#         ("What is 2 + 2?", "4"),
#         ("What is the largest planet?", "Jupiter")
#     ]
    
#     score = 0
#     time_limit = 10  # seconds

#     for question, correct_answer in questions:
#         print(question)
#         start_time = time.time()
        
#         while time.time() - start_time < time_limit:
#             user_answer = input("Your answer: ")
#             if user_answer.lower() == correct_answer.lower():
#                 print("Correct!")
#                 score += 1
#                 break
#             else:
#                 print("Incorrect!")
#                 break
#         else:
#             print("Time's up!")
    
#     print(f"Your final score is: {score}/{len(questions)}")
