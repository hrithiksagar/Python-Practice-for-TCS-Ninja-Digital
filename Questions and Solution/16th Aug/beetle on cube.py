# finding area in 3d coordinate
from math import pi
from math import sqrt
from math import pow
# sample input=
# 3
# 1,1,10, 2,1,10, 0,5,9
# formula for finding distance, from one arc to other arc
# x1 = distance 1
x1 = pi / 3 * (sqrt(1) / 2)
print(x1)
# x2 distance 2,from one side to other side
x2 = sqrt(20) + 1
print(x2)
print(5.50 + 0.50)
# case 1, (if case)When arc makes angle 60, formula to calculate distance of arc = 2*pi*r/6 = pi*r/6
# else case: [root over((x2,x1)^2 + (y2-y1)^2 + (z2-z1)^2)]



Saptarshi Please check the solution.
from math import pi def calculate_distance(point_1, point_2):
for i in range(3):
if point_1[i] in [0,10]:
surface_1 = i
if point_2[i] in [0,10]:
surface_2 = i if surface_1 == surface_2:
radius = 0
for i in range(3):
if i != surface_1:
radius += (point_1[i] – point_2[i])**2
radius = radius**(0.5)
return round(2*pi*radius/6,2) else:
height = abs(point_1[surface_1] – point_2[surface_1]) + abs(point_1[surface_2] – point_2[surface_2]) index = 3 – surface_1 – surface_2
base = abs(point_1[index] – point_2[index]) return round(((height)**2+(base)**2)**(0.5), 2) N = int(input())
coordinates = list(map(int, input().split()))
point_1 = coordinates[:3]
total_distance = 0
for i in range(1,N):
point_2 = coordinates[i*3 : (i+1)*3]
total_distance += (calculate_distance(point_1, point_2))
point_1 = point_2.copy() print(round(total_distance, 2))