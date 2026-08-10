#thread-------------------------------------------------------------
# import threading

# def work():
#     print("thread is running")
# t1 = threading.Thread(target=work)#create a thread
# t1.start()#start thread
# t1.join()#waits before main program execution

#eg=


import threading
import time
lock = threading.lock()
def work(name):
    if lock:
        for i in range(1,6):
            print(name,i)
            time.sleep(1)

t1 = threading.thread(target=work,args=("amby,"))#create a thread
t2 = threading.thread(target=work,args=("anas,"))#create a thread
t1.star()
t2.start()
t1.join()#waits before main program execution
t2.join()

    