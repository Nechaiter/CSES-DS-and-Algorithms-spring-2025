def count_rounds(numbers):
    rounds=1
    indices=[None]*len(numbers)
    for idx, i in enumerate(numbers):
        indices[i-1]=idx
    print(indices)
    for x in range(len(indices)-1):
        print(indices[x],indices[x+1])
        if indices[x]>indices[x+1]:
            rounds+=1
    return rounds





print(count_rounds([1, 2, 3, 4])) # 1
print(count_rounds([1, 3, 2, 4])) # 2
print(count_rounds([4, 3, 2, 1])) # 4
print(count_rounds([1])) # 1
print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

# n = 10**5
# numbers = list(reversed(range(1, n+1)))
# print(count_rounds(numbers)) # 100000