import math
def area(n, s):
    area = (n*s**2)/(4*math.tan(math.pi/n))
    return area
n = int(input())
s = int(input())
area = area(n, s)
print(area)
