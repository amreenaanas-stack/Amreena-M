def update_tasks():
    conn = sqlite3.connect("demo.db")
    Cursor=conn.cursor()
    td = int(input("enter tasks id : - "))
    tname = input("enter tasks name : - ")
    tdes = input("enter tasks des :-")
    cursor.execute('''
          UPDATE TASK SET name = ?,des = ?, WHERE id = ?
                 ''',(tname,tdes,td))
    conn.commit()
print("task updated")



def delettasks():
    conn = sqlite3.connect('third.db')
    cursor = conn.cursor()
    t_id = int(input('enter your task id : - '))
    choose = input('Are you sure you want to delete task y/n \n : -')

    if choose == 'y':
        cursor.execute('''

            DELETE FROM Tasks WHERE id = ?

        ''', (t_id,))
        conn.commit()
        print('TASk deleted')
    else:
        print('task not deleted')
def main():
    while True:
        print('-------Main Menu---------')
        print('------------------------- Welcome 🤗 to Task Management -------------------------')
        print("1.Register\n2.Login\n3.Exit")
        ch = int(input('enter your choice:------'))
        if ch == 1:
            register()
        elif ch == 2:
            user_id = login()
            main1(user_id)
        elif ch == 3:
            break
        else:
            print('invaid option')



import sqlite3

conn = sqlite3.connect('demo.db')

cursor = conn.cursor()

cursor.execute('''
               
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20) UNIQUE ,
            password  TEXT
               )''')

cursor.execute('''
     CREATE TABLE IF NOT EXISTS Tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,             
            name VARCHAR(30),
            desc TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
                  )
''')
