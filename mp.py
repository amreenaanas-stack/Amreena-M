#multiprocessing-----------------------------------------
# from multiprocessing import Process
# import os
# def work():
#     print("am working")
#     print(os.getpid())

# p1 = Process(target=work)
# p2 = Process(target=work)
# if __name__ == "__main__":
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()





from multiprocessing import Process
import os
X = 5
def work():
    global X
    X = X * 10
    print("am working",X)
    print(os.getpid())

p1 = Process(target=work)
p2 = Process(target=work)
if __name__ == "__main__":
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    