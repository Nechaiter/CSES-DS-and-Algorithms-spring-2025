def find_distances(street):
    one_index=[]
    for idx, i in enumerate(street):
        if i=="1":
            one_index.append(idx)
    j=0
    if len(one_index)==len(street):
        distances=[0]*len(street)
        return distances
    distances=[]
    for i in range(len(street)):
        if len(one_index)==1:
            distances.append(abs(i-one_index[j]))
            continue
        if one_index[j]==one_index[-1]:
            distances.append(abs(i-one_index[j]))
        else:
            if abs(i-one_index[j])<abs(one_index[j+1]-i):
                distances.append(abs(i-one_index[j]))
            else:
                distances.append(abs(one_index[j+1]-i))
                j+=1
    
    return distances

print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

n = 10**5
street = "0"*n + "1" + "0"*n
distances = find_distances(street)
print(distances[1337]) # 98663