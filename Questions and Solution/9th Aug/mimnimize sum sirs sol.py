n,k = map(int, input().split())
l = list(map(int, input().split()))
for i in range(k):
    a = l.index(max(l))# gives index of maximum number ii the list and stores tht in a
    l[a] = l[a]//2
print(sum(l))