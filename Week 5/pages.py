def create_string(pages):
    pages_copy=pages.copy()
    pages_copy.sort()
    string=str(pages_copy[0])
    start=0
    end=0
    for i in range(len(pages_copy)):
        
        if pages_copy[i]-pages_copy[end]<=1:
            end=i
            continue
        if pages_copy[i]-pages_copy[end]>1:

            if pages_copy[end]==pages_copy[start]:
                string=string+','+str(pages_copy[i])
            else:
                string=string+'-'+str(pages_copy[end])+','+str(pages_copy[i])
            start=i
        end=i

    if string[-1]!=str(pages_copy[end])[-1]:
        string=string+'-'+str(pages_copy[end])
    return string



print(create_string([1])) # 1
print(create_string([1, 2, 3])) # 1-3
print(create_string([4, 9, 3])) # 1
print(create_string([1, 2, 1, 2])) # 1-2
print(create_string([1, 6, 2, 5])) # 1-2,5-6
print(create_string([1, 3, 5, 7])) # 1,3,5,7
print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

pages = [3, 2, 1, 3, 2, 1]
print(create_string(pages)) # 1-3
print(pages) # [3, 2, 1, 3, 2, 1]