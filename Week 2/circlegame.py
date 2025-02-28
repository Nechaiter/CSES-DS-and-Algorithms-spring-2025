def find_order(n):
    leaved=[]
    still=list(range(1, n+1))
    while(True):
        for idx, i in enumerate(still):
            #print(idx, "% 2", idx%2)
            if idx%2!=0:
                leaved.append(i)
            else:
                still.append(i)
            #print(still)
        return(leaved)        
    
print(find_order(1)) # [1]
print(find_order(2)) # [2, 1]
print(find_order(3)) # [2, 1, 3]
print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

order = find_order(10**5)
print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]