def count_rounds_dict(numbers):
    n = len(numbers)
    
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
        
    rounds = 1
    for i in range(0, n-1):
        if pos[i + 1] < pos[i]:
            rounds += 1
    return rounds



def count_rounds_list(numbers):
    rounds=1
    indices=[None]*len(numbers)
    for idx, i in enumerate(numbers):
        indices[i-1]=idx
    for x in range(len(indices)-1):
        if indices[x]>indices[x+1]:
            rounds+=1
    return rounds


import random
import time



n=10**7
random.seed(1337)


numbers=random.sample(range(n),n)
start_time = time.time()
result = count_rounds_dict(numbers)
end_time = time.time()
print("time:", round(end_time - start_time, 5), "s")

start_time = time.time()
result = count_rounds_list(numbers)
end_time = time.time()
print("time:", round(end_time - start_time, 5), "s")