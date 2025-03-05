def count_sublists(numbers, x):
    count = {0: 1}
    prefix_sum = 0
    result = 0
    
    for i in range(len(numbers)):
        prefix_sum += numbers[i] #suma desde 0 a posicion actual
        if prefix_sum - x in count: #prefix_sum - x, suma desde 0 a i menos la suma que queremos
            print(prefix_sum - x,"prefix_sum - x")
            print(count[prefix_sum - x],"count[prefix_sum - x]")
            result += count[prefix_sum - x]

        
        if prefix_sum not in count: #la suma total este en la cuenta de las sumas?
            count[prefix_sum] = 0 #guardamos que la suma total se guarde como cero
        count[prefix_sum] += 1  #le agremos 1 a la suma
    print(count)
    return result   


# numbers=[2,3,5,-3,4,4,6,2]
# x=5
# print(count_sublists(numbers,x))

def create_distribution(string):
    length = len(string)
    substrings = set()

    for start in range(length):
        print(length)
        for end in range(start + 1, length + 1):
            print(start,end)
            print(string[start:end])
            substring = string[start:end]
            substrings.add(substring)

    distribution = {}
    for substring_length in range(1, length + 1):
        distribution[substring_length] = 0

    for substring in substrings:
        distribution[len(substring)] += 1

    return distribution

# print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}



def max_length(songs):
    n = len(songs)
    
    pos = {}
    start = 0
    length = 0
    
    for i, song in enumerate(songs):
        if song in pos:
            start = max(start, pos[song] + 1)
        length = max(length, i - start + 1)
        pos[song] = i
        
    return length
print(max_length([1,2,1,3,5,4,3,1]))