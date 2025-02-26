def find_segments(data):
    segments=[]
    count=0
    
    for i in range(len(data)):
        if i==0:
            count=1
        else:
            if data[i-1]==data[i]:
                count+=1
            else:
                segments.append((count,data[i-1]))
                count=1
    segments.append((count,data[i]))

    return segments
