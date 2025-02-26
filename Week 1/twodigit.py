def count_numbers(a, b):
    count=0
    while a<=b:
        number_length=len(str(a))
        matches=0
        loop=0
        for j in str(a):
            loop+=1
            if j not in {"2","5"}:
                if a>=10 and loop==1:
                    # a=a+1*10**(number_length-1)
                    right_digit=1*10**(number_length-1)
                    #a=a+(right_digit*2-a)
                    a=a+right_digit-a%right_digit
                    break
                else:
                    if a>=10:
                        a=a+1*10**(number_length-(loop))
                        break
                a+=1
            else:
                matches+=1
                if matches==number_length:
                    count+=1
                    a+=1
    return count

print(count_numbers(1, 100)) # 6
print(count_numbers(60, 70)) # 0
print(count_numbers(25, 25)) # 1
print(count_numbers(1, 10**9)) # 1022
print(count_numbers(123456789, 987654321)) # 512