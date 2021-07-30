def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def prime(n):
    prime_numbers = [2,3]
    i=3
    if(0<n<3):
        return prime_numbers[n-1]
    elif(n>2):
        while (True):
            i+=1
            status = True
            for j in range(2,(i//2)+1):
                if(i%j==0):
                    status = False
                    break
            if(status==True):
                prime_numbers.append(i)
            if(len(prime_numbers)==n):
                break
    return prime_numbers[n-1]
num = int(input())
if num%2==0:
    print(prime(num//2))
else:
    print(fib(num//2+1))