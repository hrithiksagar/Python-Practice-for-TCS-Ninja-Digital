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

# import math
# n = int(input())
# print("A = ",int(math.log2(n)),"\nL = ",n - 2**int(math.log2(n)))
# print("2(L) + 1 =",2 * (n - 2**int(math.log2(n))) + 1)