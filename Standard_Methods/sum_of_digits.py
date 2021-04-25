def sumOfDigits(n):
    if len(str(n))==1:
        return n
    else:
        s = sum(str(map(int, n)))
        sumofDigits(n)
        
#print(sumOfDigits(123456789))
