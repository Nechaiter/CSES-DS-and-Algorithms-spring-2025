def find_rounds(numbers):
    rounds=[]
    x=1
    while(len(numbers)>0):
        round=[]
        for i in numbers:
            if i==x:
                round.append(i)
                x+=1
        for j in round:
            numbers.remove(j)
        rounds.append(round)
    return rounds            
print(find_rounds([1, 2, 3, 4]))
# [[1, 2, 3, 4]]

print(find_rounds([1, 3, 2, 4]))
# [[1, 2], [3, 4]]    

print(find_rounds([4, 3, 2, 1]))
# [[1], [2], [3], [4]]

print(find_rounds([1]))
# [[1]]

print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
# [[1], [2, 3], [4, 5, 6], [7, 8]]