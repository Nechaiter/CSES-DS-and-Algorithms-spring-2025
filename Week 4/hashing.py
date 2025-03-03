def hash_value(string):
    A=23
    M=2**32
    letter_value={}
    char2 = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(char2)):
        letter_value[char2[i]]=i

    string_sum=0
    string_lenght=len(string)
    for i in range(len(string)):
        string_sum=string_sum+(letter_value[string[i]])*A**(string_lenght-1)
        string_lenght=string_lenght-1

    return string_sum%M


print(hash_value("abc")) # 25
print(hash_value("kissa")) # 2905682
print(hash_value("aybabtu")) # 154753059
print(hash_value("tira")) # 235796
print(hash_value("zzzzzzzzzz")) # 2739360440