def count_splits(sequence):
    zeros=sequence.count("0")
    ones=sequence.count("1")
    splits=0
    left=[(0,0)]
    for i in range(len(sequence)):
        if i>0 and zeros==ones and left[0][0]==left[0][1]:
            splits+=1
        if sequence[i]=="0":
            zeros=zeros-1
            left[0]=(left[0][0]+1,left[0][1])
        else:
            ones=ones-1
            left[0]=(left[0][0],left[0][1]+1)
    return splits


print(count_splits("1011111010")) # 0    1=7 0=3


print(count_splits("00")) # 0
print(count_splits("01")) # 0
print(count_splits("0110")) # 1
print(count_splits("010101")) # 2
print(count_splits("000111")) # 0
print(count_splits("01100110")) # 3

sequence = "01"*10**5
print(count_splits(sequence)) # 99999