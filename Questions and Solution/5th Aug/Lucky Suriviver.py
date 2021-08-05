def lucky(n):
    if n%2 == 0:
        return 1
    elif n==1:
        return 1
    else:
        i = 0
        while(2**i < n):
            i+=1
        a = i -1
        l = n - (2**a)
        print((2*l)+1)
        
n = int(input("Enter total number of people: "))
print(lucky(n))