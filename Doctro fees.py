
    f = 0
    num = 0
    while(num<20):
        age = input()
        if age =="":
            break
        elif int(age)<= 0 or int(age)>=120:
            print("Not a Valid Age.")
        else:
            age = int(age)
            if age<17:
                f += 200
            elif age>=17 and age<= 40:
                f += 400
            else:
                f += 300
        num += 1


# arr = []
# for i in range(len(arr)):
#     a = int(input("Enter Ages of the patients: "))
#     a.append(arr)
# print(arr)