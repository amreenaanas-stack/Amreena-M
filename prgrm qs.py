# # 1.plot the point on a cartesian plane which has 2 cordinates x and y do tehe following ?
# #.define a class point ,its instant shuld have 2 attributes x and y x and y default value must be zero ?
# #.define an instance method reset().when called it will set x and y value to zero (that is it will set the points to origin(0,0)) ?
# #.define an method m0ve().this shuld change the values of x and y ?
# #.use this move method to update reset()method ?
# #.define 2 methods xmove and ymove.this shuld move the valuues of x and y separately ?

# # answer=
# class point:
#     def __init__ (self,x=0,y=0):
#         self.x=x
#         self.y=y
#     def reset(self):
#         self.x,self.y=0,0
#         self.move(0,0)

#     def move(self,a,b):
#         self.x=a
#         self.y=b
#     def xmove(self,a):
#         self.x=a
#     def ymove(self,b):
#         self.y=b
        
# p1=point(1.0)
# print(p1.x,p1.y)
# p1.reset()
# print(p1.x,p1.y)
# p1.move()
# print(p1.x,p1.y)

# #2. .Write a Python class Queue that implements a basic queue data structure with the enqueueand dequeue methods.?
# The enqueue method should add an element to the rear of the queue,
#  and the dequeue  method should remove and return the remaining element from the queue.
# Additionally, include a method is_empty to check if the queue is empty.

class Queue:
    def __init__(self):
        self.items = []#empty list, all list items stored this list

    def enqueue(self, item):#enqueue is a new item queue ithinte last cherkka 
        self.items.append(item)

    def dequeue (self):#dequeue is a firt item delete 
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)#it is a first item delete cheyyum

    def is_empty(self):
        return len(self.items) == 0 #queue empty aano enn checking                                 
q1=Queue()    
q1.enqueue("A")
q1.enqueue("B")
q1.enqueue("C")
print(q1.items)
print(q1.dequeue())
print(q1.is_empty())
