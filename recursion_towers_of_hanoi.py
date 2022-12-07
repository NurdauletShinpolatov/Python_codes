def towers_of_hanoi(n, start, end):
    if n==1:
        print(start, "-->", end)
    else:
        towers_of_hanoi(n-1, start, 6-start-end)
        print(start, "-->", end)
        towers_of_hanoi(n-1, 6-start-end, end)
print("Welcome to towers of hanoi. I will say the moves to solve your problem if it has 3 columns, for that...")
n = int(input("Enter the number of block at tower\nn: "))
start = int(input("Enter the start position of tower\nstart: "))
end = int(input("Enter the end position where tower should be in order to win\nend: "))
towers_of_hanoi(n, start, end)
