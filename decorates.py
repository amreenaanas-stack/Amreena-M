# #decorates--------------------------------------
# # functions that enhance other functions
# # it is a higher order functions
# # higher order functions is a a function as its arguments or return a function
# # *args* *kwrgs*

# def saymyname(fun):
#     def wrapper():
#         print("say my name")
#         fun()
#         print("you are right")
#     return wrapper
# @saymyname
# def add():#ithil add anu function
#     print("add 2 numbers")
# add()#function call

# #*args* ------------------------------
# # #*args 
# # #positional arguments
# # def add(*args):
# #     return args
# # print(add(2,5,8,65,55,4,454,87,8,87,787,8,878,4455,545))


# # #**kwargs----------------------------------------

# # #keyword arguments
# def fullname(**kwargs):
#     print(kwargs)
# fullname(fname="amre", mname="ena", lname="m" ,tnam="anas")

# #time module-----------------------
# import time 
# print(time.time())#curret local time in second
# print(time.time())#current local time
# print(time.ctime(12345666.66666789))
# start=time.time()
# for i in range(1,11):
#     print(i)
#     time.sleep(1)
# stop = time.time()
# print("total time:",stop-start)

import time
def totaltime(n):
    def innner(fun):
        def wrapper(*args,**kwargs):
            start = time.time()
            fun(*args,**kwargs)
            stop = time.time()
            print(f"total time : {stop-start}")
        return wrapper
    return innner
@totaltime(10)
def myname(n):
    for i in range(n):
        print(i)
        time.sleep(1)
myname(2)


                         