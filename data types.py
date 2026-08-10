a=6
print (type(a))

#int
a=6
name='mohan'
print (type (name))
a=0
print(a)
print (type(a))

#floating
b=5.0
print(b)
print(type(b))


#boolean
a=True
b=False
print(a)
print(type(a))
print(type(b))


#list---------------
#lists are ordered and changeable

#list can have any element of any size
data = [1,2 , 3 , "mohan", True, [12, 131, 14]]
#list is a collection of elements
#list are defined by square brackets []
#lists are ordered
a= [1,2,3,4,5]
b=[  3,1,2,4,]
print(a==b)
#list are indexed
#0  1 2 3 4 
a=[11,12,13,14,15,16,17,18,19]
print(a)
print(a[1])
print(a[3:8])
print(a[0:9:2])
print(a[:7])
print(a[4:])
print(a[::-1])
b=[8,7,6,5,4,3,2,1]
print(b)
#LIST ARE MUTABLE (CHANGABLE)
c=[11,12,13,14,15]
c[0]="MOHAN"
print(c)
#str immutable 



#list are nested
a=(11,12,[100,200],13,14)
b=a[2]
print(b[0])
print(a[2][0])

#inbuilt methods------------------
#to add elements 
#append()
#adds an element to the end of the list
a=[11,12,13,14,15]
a.append(100)
a.append(200)
print(a)
#extend()
#adds all the elements of an iterable to the end of the list
a=[11,12,13,14,15]
a.extend([24,23,"mohan"])
print(a)
#insert()
#adds an element at a specified position
a=[11,12,13,14]
a.insert(1,"mohan")
print(a)
#remove()
#removes the first occurrence of an element from the list
a=[11,12,13,14,15]
a.remove(13)
print(a)

a=[11,12,13,14,15,13,13,13]
a.remove(13)
print(a)
#pop()
#last elements is removed from the list
a=[11,12,13,14,15]
a.pop()
print(a)
#popnte ullil 0 kodthal first element remove aagum 
a=[11,12,13,14,15]
a.pop(0)
print(a)

#tuple()----------------
#defined by parentheses "()"
#collectio of data 
#tuples are ordered and unchangeable (immutable)
#indexed
b=(16,17,18,18,20)
print(b[0])


#iteration------------
#for i in range (0,len(a)):
#    print(a[i])
fruits = ["apple", "banana", "cherry"]
for i in range (0, len(fruits)):
    print(i, fruits[i])






