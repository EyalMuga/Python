# import threading
#
# lock1 = threading.Lock()
#
# counter = 0
#
# def a():
#     lock1.acquire()
#     print("Inside critical section of a")
#     c()
#     lock1.release()
#
# def c():
#     lock1.acquire()
#     print("Inside critical section of c")
#     lock1.release()
#
#
# # what will be the outout?
# a()
#
# ######

import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

counter = 0


def a():
    print("a waiting for lock 1")
    lock1.acquire()
    print("a acquired  lock 1")
    print("Inside critical section of a, acquired lock 1")
    c()
    lock1.release()


def b():
    print("b waiting for lock 1")
    lock1.acquire()
    print("b acquired  lock 1")
    print("Inside critical section of b, acquired lock 1")
    lock1.release()


def c():
    print("c waiting for lock 2")
    lock2.acquire()
    print("c acquired  lock 2")
    print("Inside critical section of c, acquired lock 2")
    b()
    lock2.release()


t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)
t1.start()
t1.join()

t2.start()
t2.join()
