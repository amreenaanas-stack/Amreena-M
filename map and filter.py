#map-----------------------------------------------------
#adds an iterable to a function
#map is a object or oop
#map(functon,iterable)

# def square(z):
#     return z**2


products = [
("nike x11",178),
("apple watch", 456),
("samsung s24",999),
("ps5 pro",700),
("iphone", 1100)
]
def toINR(z):
    return z[1]*96,34
result = map(toINR,products)
print(list(result))

#filter------------------------------------------
def iseven(a):
    if a%2 == 0:
        return a 
a = [1,2,3,4,5,6,7,8,9,10]