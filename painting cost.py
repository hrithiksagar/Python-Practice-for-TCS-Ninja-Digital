# i = 18/sq feet
# e = 12/sq feet

    

i = float(input("Enter number of interior walls: "))
e = float(input("Enter number of Exterior Walls: "))
for a in range(0,i):
    si = (input("Enter Surface Area of Interior Walls:"))
for b in range(0,e):
    se = (input("Enter Surface Area of Exterior Walls:"))
total = sum([a*18 for a in si])+sum([b*18 for b in se])
print(total)