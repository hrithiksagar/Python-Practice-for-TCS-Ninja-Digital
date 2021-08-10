
# There are n stairs, a person standing at the bottom wants to reach the top.
# The person can climb either 1 stair or 2 stairs at a time. 
# Count the number of ways, the person can reach the top.
# Consider the example shown in the diagram. The value of n is 3. There are 3 ways to reach the top. The diagram is taken from Easier Fibonacci puzzles

# Examples: 

# Input: n = 1
# Output: 1
# There is only one way to climb 1 stair

# Input: n = 2
# Output: 2
# There are two ways: (1, 1) and (2)

# Input: n = 4
# Output: 5
# (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2) 


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


s = int(input())
print("Number of ways are: ")
print(fib(s+1))

