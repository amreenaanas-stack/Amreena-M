#Nested loops(loopinte akath loop kodukkuka)------------------
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            print(i,j,k) 

#another exaple
for i in range(5,10):
    for j in range(3,6):
        for k in range(6,9):
            print(i,j,k)  

#creating pyramid using nested loop----
for i in range (1,6):
    for j in range (1,i+1):
        print("*",end="")
        print()
#o/p:
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range (1, 11):
    for j in range(1,i+1):
       print("*",end="")
    print()
#reverse aayitt cheyyuka:

for i in range (5,0,-1):
    for j in range(1,i+1):
       print("*",end="")
    print()

#with using underscore-----
for i in range(1,6):
       for j in range(6-i):
           print("_",end="")
       for k in range(1,i+1):
             print("*",end=" ")
       print()

#with using space-----
for i in range(1,6):
       for j in range(6-i):
           print(" ",end="")
       for k in range(1,i+1):
             print("*",end=" ")
       print()
       

#print chessboard pattern(my eg)--------
for i in range(1,9):
    for j in range(1,9):
        if (i + j) % 2 == 0:
            print("w" , end=" ")
        else:
            print("B" , end=" ")
    print()

#or(real easy way)(but not change)
for i in range(1,9):
    for j in range(1,9):
        if (i + j) % 2 == 0:
            print("w" , end=" ")
        else:
            print("B" , end=" ")
    print()

  

  