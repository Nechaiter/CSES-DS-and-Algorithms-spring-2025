def check_number(number):
    sum=0
    patern="371"
    patern_n=0
    if number[0]!="0" or len(number)!=9:
            return False
    for i in range(len(number)-1):
        sum=(int(number[i])*int(patern[patern_n]))+sum
        if patern_n==2:
            patern_n=0
        else:
            patern_n+=1
    if sum%10>0 and 10-(sum%10)==int(number[len(number)-1]):
        return True
    else: 
        if sum%10==0 and 0==int(number[len(number)-1]):
            return True
    return False
