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


numbers=[2,3,5,-3,4,4,6,2]
x=5
print(count_sublists(numbers,x))



for i in range(n):
        if b == len(right) or \
           (a < len(left) and left[a] < right[b]):
            items[i] = left[a]
            a += 1
        else:
            items[i] = right[b]
            b += 1