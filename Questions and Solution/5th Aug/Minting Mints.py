# inputs:
"""
n = number of mints 1st person have (2<n<10)
len = length of the row (1<len<20)
"""


# # Hrithiks Code
# def mints(n, len):
#     for i in range(1, len + 1):
#         total = len / 2((2 * n) * [(len - 1) * (n - 1)])
#         i += 1
#     return int(total)
#
#
# n = int(input("Enter mints 1st person have: "))
# len = int(input("Enter length of the row:"))
# print("Total number of mints are:", mints(n, len))

# # Vineeth Kumar code:
# n = int(input())
# l = int(input())
#
# if n in range(2, 11) and l in range(1, 21):
#     for x in range(l):
#         if x == 0:
#             sum = n
#         else:
#             sum = sum + (sum - 1)
#
# print(sum)

# def mintss(n, l):
#     if n in range(2, 11) and l in range(1, 21):
#         for x in range(l):
#             if x == 0:
#                 sum = n
#             else:
#                 sum = sum + (sum - 1)
#     return sum
#
#
# n = int(input("Enter mints 1st person have: "))
# l = int(input("Enter length of the row:"))
# print("Total number of mints are:", mintss(n, l))

#Shriyans Code:
sum, n = [int(x) for x in input().split()]
if sum < 2 or sum>10 or n < 1 or n > 20:
    print("INVALID INPUT")
    exit()
i = 1

while(i < n):
    sum += sum - 1
    i += 1

print(sum)