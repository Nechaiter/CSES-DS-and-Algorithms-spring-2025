import random
import time

def added(list,n):
    for i in range(n):
        list.append(i)
def deleted(list,n):
    for i in range(n):
        list.pop()
n = 10**5
print("n:", n)
list=[]

start_time = time.time()
added(list,n)
end_time = time.time()
print("time:", round(end_time - start_time, 4), "s")

start_time = time.time()
deleted(list,n)
end_time = time.time()
print("time:", round(end_time - start_time, 4), "s")
