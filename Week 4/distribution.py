def create_distribution(string):
    distribution={}
    patterns=set()
    concatt=""

    for i in range(len(string)):
        concatt=concatt+string[i]
        if concatt not in patterns:
            patterns.add(concatt)
            
            if len(concatt) in distribution:
                distribution[len(concatt)]=distribution[len(concatt)]+1
                #print(concatt,len(concatt),distribution[len(concatt)])
            else:
                distribution[len(concatt)]=1
                #print(concatt,len(concatt),distribution[len(concatt)])
        if string[i] not in patterns:
            patterns.add(string[i])
            if len(string[i]) in distribution:
                distribution[len(string[i])]=distribution[len(string[i])]+1
                #print(string[i],len(string[i]),distribution[len(string[i])])
            else:
                distribution[len(string[i])]=1
                #print(string,len(string[i]),distribution[len(string[i])])
        for j in range(i):
            if concatt[j:] not in patterns and concatt[1:]!='':
                patterns.add(concatt[j:])
                if len(concatt[j:]) in distribution: 
                    distribution[len(concatt[j:])]=distribution[len(concatt[j:])]+1
                    #print(concatt[j:],len(concatt[j:]),distribution[len(concatt[j:])])
                else:
                    distribution[len(concatt[j:])]=1
                    #print(concatt[j:],len(concatt[j:]),distribution[len(concatt[j:])])
    return dict(sorted(distribution.items()))
        


print(create_distribution("aaaa"))
# {1: 1, 2: 1, 3: 1, 4: 1}

print(create_distribution("abab"))
# {1: 2, 2: 2, 3: 2, 4: 1}

print(create_distribution("abcd"))
# {1: 4, 2: 3, 3: 2, 4: 1}

print(create_distribution("abbbbbb"))
# {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

print(create_distribution("aybabtu"))
# {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}