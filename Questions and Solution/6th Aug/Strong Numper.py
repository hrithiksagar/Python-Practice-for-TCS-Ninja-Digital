# Strong Number
# Given a number
# "n' we have to check whether the number given is Strong Number or not.
# Strong number is a number whose sum of all digits' factorial is equal to the number 'n'. Factorial implies when we
# find the product of all the numbers below that number including that number and is denoted by ! (Exclamation sign),
# For example: 4!
# = 4x3x2x1 = 24.
# SO,,
# to find a number whether its strong number, we have to pick every digit of the number like the number is 145 then
# we have to pick 1, 4 and 5 now we will find factorial of each number i.e, 1! =
# 1, 4! = 24, 5! = 120.
# Now we will sum up 1 + 24 + 120 so we get 145, that is exactly same as the input given, So we can say that the number
# is strong number.
# Example
# Input: n = 124
# Output: No it is not a strone number
# Explanation: 1! + 2! + 4! = 27 which is not equal to n i.e, 124
# Inout: n= 145
# Output: Yes it is a strone number
# Explanation: 1! + 4! + 5!
# =145
from math import factorial
n = input("enter a number ")
s = sum([factorial(int(x)) for x in n])
if int(n) ==s:
    print("Strong number")
else:
    print("Not Strong Number")
    