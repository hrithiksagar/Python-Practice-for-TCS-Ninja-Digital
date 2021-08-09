lst = []
n = int(input("enter number of elements: "))
k =int(input("enter maximum operations on elements: ")) 
for i in range(0,n):
    m = int(input("enter elements"))
    lst.append(m)
print(lst)
for ele in range(k):
    for i in lst:
        m = max(lst)/2
        i += 1
    print(lst)
print(lst)
        
