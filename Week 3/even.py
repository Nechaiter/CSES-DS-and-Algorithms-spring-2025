def count_sublists(numbers):
    
    count=0
    previous=0
    a=0
    b=0

    for i in range(len(numbers)):
        
        if numbers[i]%2==0:
            count+=1
            if previous>0:
                a=i
                count+=a-b
            else:
                b=i
            previous+=1
        else:
            previous=0
    return count




print(count_sublists([2, 4, 1, 6])) # 4
print(count_sublists([1, 2, 3, 4])) # 2
print(count_sublists([1, 1, 1, 1])) # 0
print(count_sublists([2, 2, 2, 2])) # 10
print(count_sublists([1, 1, 2, 1])) # 1

numbers = [2] * 10**5
print(count_sublists(numbers)) # 5000050000