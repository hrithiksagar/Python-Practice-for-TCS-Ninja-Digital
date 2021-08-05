first, second, nth = [int(i) for i in input().split()]
i = 2
if(nth == 1):
    print(first)
    exit()
elif(nth == 2):
    print(second)
    exit()
while(i < nth):
    res = first + second
    first,second = second,res
    i += 1
print(res)