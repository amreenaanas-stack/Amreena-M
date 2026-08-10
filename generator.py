#generator---------------------------------------
# def mydata():
#     yeild "one"
#     yeild "two"
#     yeild "three"
#     yeild "four"
#     yeild "five"
#     yeild "six"

# #a = mydata()
# print (next(a))
# print (next(a))
# print (next(a))

# b = []
# i = 0 
# while true:
# b.append 
# i = i +1



def inifinz():
    i=1
    while True:
        yield i
        i = i + 1

inifine_number = inifinz()
print(inifine_number)
for i in inifine_number:
    print(i)