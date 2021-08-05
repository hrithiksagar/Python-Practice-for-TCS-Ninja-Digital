n = int(input("Enter the number of people: "))
start = int(input("Enter the starting point: "))
direction = int(input("Enter 0 for anticlockwise direction and 1 for clockwise direction: "))
k = int(input("Enter the nth person who are going to be executed:"))

seating = [int(i) for i in range(1,n+1)]

def clockwiseDirection(seating, start, k):
    jump = start + k -1
    print("Deleting",end = " ")
    while(len(seating) > 1):
        # jump += k
        if(jump >= len(seating)):
            jump = jump % len(seating)
        print(seating[jump], end = " ")
        seating.remove(seating[jump])
        jump += k-1

    print("\nThe Lucky Survivor", seating[0])

def anticlockwiseDirection(seating, start, k):
    jump = start - k - 1
    print("Deleting",end = " ")
    while(len(seating) > 1):
        if(jump < 0):
            jump = len(seating) + jump
        print(seating[jump], end = " ")
        seating.remove(seating[jump])
        jump -= k

    print("\nThe Lucky Survivor",seating[0])

if(start > n):
    print("Try again, Starting point needs to be less than number of people")
else:
    if(direction == 0):
        anticlockwiseDirection(seating, start, k)
    elif(direction == 1):
        clockwiseDirection(seating, start, k)
    else:
        print("Try again, enter 0 for anticlockwise direction and 1 for clockwise direction")