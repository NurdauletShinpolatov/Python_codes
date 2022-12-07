# // TRIANGLE IN 2D ARRAY
# // This program outputs atriangle in square which has
# // common side.

side = int(input("Enter the length of side of square: "))
array = [[0 for x in range(side)] for y in range(side)]

n1 = side   # // number of "1" in one row
n0 = 0      # // number of "0" on one side of "1"s
for row in range(side):
    for zeroes in range(n0):    # // before "1"
        array[row][zeroes] = 0  
    for ones in range(n1):      # // "1"s
        array[row][ones] = 1
    for zeroes in range(n0):    # // after "1"
        array[row][zeroes] = 0
    n0 += 1
    n1 -= 1


for ROW in range(side): # // outputing the square
    for COLUMN in range(side):
        print(array[ROW][COLUMN], end=" ")
    print()
