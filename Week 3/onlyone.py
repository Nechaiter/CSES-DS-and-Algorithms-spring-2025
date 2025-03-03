def find_number(numbers):
    each=[]
    f=numbers[0]
    each.append((f,1))
    for i in range(len(numbers)-1):
        if f!=numbers[i+1]:
            each.append((numbers[i+1],1))
        else:
            each[0]=(f,each[0][1]+1)
    for i in each:
        if i[1]==1:
            return i[0]
            
    return "Error"


print(find_number([1, 1, 1, 2])) # 2
print(find_number([1, 1, 2, 1])) # 2
print(find_number([1, 2, 1, 1])) # 2
print(find_number([2, 1, 1, 1])) # 2
print(find_number([5, 5, 5, 3, 5])) # 3
print(find_number([1, 100, 1])) # 100

numbers = [1] * 10**5 + [2]
print(find_number(numbers)) # 2