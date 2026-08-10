# database-----------------------------
# data is a information
# data base is 2 types

# 1.relational database
# data contained(hold)  table format(rows and columns)
# sql - structured query language(its a language)
# eg= MySQL, postgersql

# 2.non relational database
# data contained records(files)

#sqlite------------------------(database connect cheyyunna reethi)
import sqlite3
conn = sqlite3.connect("first.db") #establishing a connection to the db
cursor = conn.cursor() #to intract with the database

#operations--------------------------------
cursor.execute
(
    ''''
    CREATE TABLE IF NOT EXIST student(
        name VARCHAR(20),
        age INTEGER,
        adress TEXT
    )
   '''
)
conn.close()

def addstudent():
    conn = sqlite3.connect("first.db") #establishing a connection to the db
    cursor = conn.cursor()
    student_name = input("enter student name : - ")
    student_age = int(input("enter student age : -" ))
    student_address = input("enter student address")
    cursor.execute('''
          INSERT INTO student(name,age,address)
                   VALUES(?,?,?)
        ''',(student_name,student_age,student_address))
    conn.commit()
    print("student added")


    conn.close()


def main():
    while True:
        print("welcome to student management")
        ch = int(input("1.ADD STUDENT\n2.VIEW STUDENT"))
        if ch == 1:
            addstudent()
        else:
            print("invalid choice")







