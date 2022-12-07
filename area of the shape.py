# 1.2-1.0 
# should be tested 
import math
cors = input("Enter the cordinates of points: ").split()
area = 0
# input should be in this format:
# 0,0 1,0 1,1 0,1


def length(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def triangles_area(x1, y1, x2, y2, x3, y3):
    global area
    a = length(x1, y1, x2, y2)
    b = length(x2, y2, x3, y3)
    c = length(x3, y3, x1, y1)
    p = 0.5*(a+b+c)
    area += math.sqrt(p*(p-a)*(p-b)*(p-c))


def dividing_into_triangles():
    x1, y1 = float(cors[0][:cors[0].find(",")]), float(cors[0][cors[0].find(",")+1:])
    for i in range(1, len(cors)-1):
        x2, y2 = float(cors[i][:cors[i].find(",")]), float(cors[i][cors[i].find(",")+1:])
        x3, y3 = float(cors[i+1][:cors[i+1].find(",")]), float(cors[i+1][cors[i+1].find(",")+1:])
        triangles_area(x1, y1, x2, y2, x3, y3)

        
dividing_into_triangles()
print("Area =", area)
















