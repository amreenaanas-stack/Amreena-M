#recursion------------------------------
# higher order functions
# when a function get a function as its argument 
# when a function returns a function 
#function called itself is called recursion

# def hello():
#     return hello()
# print("mohan")
# print(hello())
# hello()

#10numbers
# def counttozero(n):
#     print(n)
#     if n==0:
#         return #sttop the recursion
#     return counttozero(n-1) #condition for recursion
# counttozero(10)

#sum =using recursion() ?
# def sumtozero(n):
#     if n==0:
#         return 0
#     return n + sumtozero(n-1)
# print(sumtozero(10))

# #factorial=using recursion ?
# def factorial(n):
#     if n==0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))



#SCOPE OF VARIABLES--------------------------------(VERY IMPORTANT)
#area in which its is recoganaized
# name="amby"#global scope
# def myname():
#     name="amreena"
#     def nickname(): #local scope
#         name="anas"
#         print(name)
#     nickname()
# myname()
#L E G B 
#GLOBAL ENCLOSING LOCAL BUILT-IN