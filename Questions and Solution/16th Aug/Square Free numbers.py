"""
Square free number
In the theory of numbers, square free numbers have a special place.
A square free number is= Number that is not divisible by a perfect square (other than 1).
Example:
Thus 72 is divisible by 36 (a perfect square), and is not a square free number,
but 70 has factors 1, 2, 5, 7, 10, 14, 35 and 70.
As none of these are perfect squares (other than 1), 70 is a square free number.

==
For some algorithms, it is important to find out the square free numbers that divide a number.
Note: 1 is not considered a square free number.
==
Input:
The only line of the input is a single integer N which is divisible by no prime number larger than 19
Output:
One line containing an integer that gives the number of square free numbers (not including 1)
EXAMPLE 1:
Input
20
Output
3
Explanation
N=20
If we list the numbers that divide 20, they are
1, 2, 4, 5, 10, 20
EXAMPLE 2:
Input:
72
Output:
3
Explanation
N=72. The numbers that divide 72 are
1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72
1 is not considered square free. 4, 9 and 36 are perfect squares,
and 8,12,18,24 and 72 are divisible by one of the. Hence only 2, 3 and 6 are square free.
(It is easily seen that none of them are divisible by a perfect square). The result is 3
"""

# def perfectsq(n):
#     for i in range(n):
#         if n % i == 0 and n / i == i:
#             return 1
#     return 0

import math


def sqfree(n):
    if n % 2 == 0:
        n = n / 2
    # if 2 again divides n then n is not square free no
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1)):
        # check if i is prime factor
        if n % i == 0:
            n = n / i
        # if i again divides then n is not sq free number
        if n % i == 0:
            return False
    return True


n = 72
if sqfree(n):
    print("yes")
else:
    print("No")
