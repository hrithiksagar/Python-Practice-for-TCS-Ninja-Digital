def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


s = int(input())
print("Number of ways are: ")
print(fib(s+1))