# given a set of array elements
#task : find max sum of m consecutive elements
# suppose:
# arr[] = {1,3,2,5,6}
# m =3
# so max sum of 3 consecutive elements is 2+5+6;

# for i in range(len(=res)):
#     sum = 0
#     sum += res[i]
#User input array without knowing size:
# li = [int(i) for i in input().split()] # using List Comp.
# print(li)

# import random
# res = random.sample(range(1,50),7)
# print(res)
# n = int(input("Enter a number to start summation: "))

# vineeth
# n = int(input(""))
# n = int(input))
# arr = []
# for i in range(n):
#     x = int(input())
#     arr.append()
# s = 0
# max = 

# Shriyans
li = [int(i) for i in input().split()]
m = int(input())
sum = maxSum = 0
for i in range(len(li)):
    if(i < m):
        sum += li[i]
    else:
        sum -= li[i - m]
        sum += li[i]
    if(sum > maxSum):
        maxSum = sum
print(maxSum)