def count_substrings(string):
    patterns=set()
    concatt=""

    for i in range(len(string)):
        concatt=concatt+string[i]
        if concatt not in patterns:
            patterns.add(concatt)
        if string[i] not in patterns:
            patterns.add(string[i])
        for j in range(i):
            if concatt[j:] not in patterns and concatt[1:]!='':
                patterns.add(concatt[j:])
    return len(patterns)
        


print(count_substrings("aaaa")) # 4
print(count_substrings("abab")) # 7
print(count_substrings("abcd")) # 10
print(count_substrings("abbbbbb")) # 13
print(count_substrings("aybabtu")) # 26w
print(count_substrings("saippuakauppias")) # 110