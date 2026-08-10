#for loop
#for i in range ():
   # code to be executed
for i in range (2,7,2):
    print(i)

#100 numbers sum 
sum = 0
for i in range (1,101,1):
    sum = sum + i
print(sum)


#reversebp of a number
for i in range (10,0,-1):
    print(i)

#factorial of a number 
fact=1
for i in range (5,1,-1):
 fact = fact * i
 print(fact)

# #check if a number is armstring or not (tuple[for loop])
num = 1222
temp = num
sum = 0
for i in range(temp):
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if (num == sum):
    print("armstrong")
else:
    print("not armstrong")

# check if a number is prime number (tuple[for loop])
num=int(input('enter your number:---'))
prime=True 
if num==1:
    prime=False
else:
    for i in range(2,6):
        if num % i== 0:
            prime=False
            break
if prime==True:
        print("prime number")
else:
     print("not a prime")
