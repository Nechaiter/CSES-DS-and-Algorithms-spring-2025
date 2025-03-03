def count_sublists(numbers):
    b=0
    count=0
    c=0
    for i in range(len(numbers)):
        a=numbers[i]
        # print(b,a,">",c,count)
        if a>c:
            count+=i+1-b
            
        else:
            b=i
            count+=1
        # print(b)
        # print(count)
        c=a
    return count

print(count_sublists([2, 1, 3, 4])) # 7
print(count_sublists([1, 2, 3, 4])) # 10
print(count_sublists([4, 3, 2, 1])) # 4
print(count_sublists([1, 1, 1, 1])) # 4
print(count_sublists([1, 2, 1, 2])) # 6

numbers = list(range(1, 10**5+1))
print(count_sublists(numbers)) # 5000050000