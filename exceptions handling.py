# exceptions----------------------------
# events that effect the execution of our program are called exceptions. Exceptions are errors that occur during the execution of a program. When an exception occurs, the normal flow of the program is interrupted, and the program may terminate if the exception is not handled properly
# error
# syntax error
# runtime error
# type error
# indentation error  etc....


#error varunnath=
# try:
#     a = 5
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("you have an error", e)
#     print("mohan")


#error varathath=
# try:
#     a = 5
#     b = 1
#     print(a/b)
# except Exception as e:
#     print("you have an error", e)
#     print("mohan")


# try:----------------------
#     a = int (input("enter a number:"))
#     b = 5
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero")
# except ValueError :
#     print("check values")
# except TypeError:
#     print("check types")
# finally:
#     print("this will always execute")

##zerodivision error(zero vech devide cheyyan patula athinte eg)
# try:
#     a = int(input("enter a number:"))
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero")
# except ValueError :
#     print("check values")
# except TypeError:
#     print("check types")
# finally:
#     print("this will always execute")

#type error(typr error nokkunnathinte eg)
# try:
#     a = int(input("enter a number:"))
#     b = "minnaminni"
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero")
# except ValueError :
#     print("check values")
# except TypeError:
#     print("check types")
# finally:
#     print("this will always execute")


#value error(value error nokkunnathine eg)
# try:
#     a = int(input("enter a number:"))
#     b = 5
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero")
# except ValueError :
#     print("check values")
# except TypeError:
#     print("check types")
# finally:
#     print("this will always execute")


#raise keyword--------------------
# class Myerror(Exception):
#     pass
# name = "das"
# if name == "das":
#     raise Myerror("name should not be das")
