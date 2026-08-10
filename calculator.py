
#types of arguments------------------

#1.positional arguments=
def add2(a,b):
    print(a+b)
add2(3,5)    

#2. keyword argument=
def fullname(fname,mname,lname):
    print(fname+' '+mname+' '+lname)
fullname(fname="di" , mname="ls", lname="sha")   

#default argument
def aa2(a=0,b=0):
    print(a+b)
aa2(3,4)
aa2()    



#create calculator using functions------------------------------------
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    while True:
        print("Welcome to simple calculator !!!!!!!!!!!!!!")
        ch=int(
            input("enter your choice : \n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit\n:----"))
        x=int(input("enter number :"))
        y=int(input("enter number :"))
        if ch == 1:
            print(add(x,y))
        elif ch == 2:
            print(sub(x,y))
        elif ch == 3:
            print(mul(x,y))
        elif ch == 4:
            print(div(x,y)) 
        elif ch == 5:
            break
        else:
            print("invalid choice")
main()


