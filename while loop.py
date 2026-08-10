
#sum of digits in a number
#input - 343
#op - 15 
num=12345
sum = 0
while num> 0:
    b=num %10
    sum = sum+b
    #print (num)
    num=num // 10
print(sum)




#reverse of a number
#num=12345
#op=54321
num=12345
rev=0
while num>0:
    b=num%10
    rev=rev*10+b
    num=num//10
print(rev)



#factorial of a number
#num=4
#0P=4*3*2*1
fact=1 
for i in range(5,1,-1):
     fact=fact*i
print(fact)



#average of n numbers
count = int(input('enter num count:-"))'))
sum=0
for i in range (count):
    num=int(input("enter num:-"))
    sum=sum+num
print(f"sum is {sum}")
print(f"average = {sum/count}")


