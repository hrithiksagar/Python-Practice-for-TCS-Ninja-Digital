t1=0
t2=0
t3=0
for i in range(1,10):
    n = int(input())
    if n not in range(1,101):
        print("Invalid")
        exit()
    if i%3 ==1:
        t1+= n
    if i%3 ==2:
        t2+=n
    else:
        t3 += n
        

maxavg = max(t1, t2,t3)
if maxavg < 210:
    print("All trainees are unfit")
else:
    if t1 == maxavg:
        print("Trainee # : ", 1)
    if t2 == maxavg:
        print("Trainee # : ", 2)
    if t3 == maxavg:
        print("Trainee # : ", 3)
