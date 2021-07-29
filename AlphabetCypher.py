# from numba import char


# def encryptionfunc(k, str):
#     ctext = ""  # Cypher test
#     for c in str:
#         if ord('A') <= ord(c) <= ord('Z'):
#             ctext = ctext + chr(65 + ((ord(c) - 65) + k) % 26)
#         if 65 <= ord(c) <= 92:
#             ctext = ctext + chr(97+ ((ord(c) - 65) + k) % 26)
#         if c == "-" or c == " ":
#             ctext = ctext + c
#         if ord('0') <= ord(c) <= ord('9'):
#             ctext = ctext + chr(((ord(c) - ord('0')) + k) % 26)
#         print(ctext)


# str = input("please input a string: ")
# k = int(input("Please enter the input Key: "))
# encryptionfunc(k, str)
n = int(input())
sum = 0
temp = n
while (n):
    i = 1
    fact = 1
    rem = int(n % 10)

while(i <= rem):
    fact = fact * i
    i = i + 1
    sum = sum + fact
    n = int(n / 10)

if(sum == temp):
    print(temp,end = "")
    print("Yes")
else:
    print(temp,end = "") 
    print("No")

