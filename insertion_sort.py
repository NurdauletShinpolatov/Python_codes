# // getting an array:
array = input().split()


# // sorting:
cnt = 0
while True:
    cnt += 1
    stop = True
    for i in range(len(array)-cnt):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            stop = False


            for j in range(i, 0, -1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    print("pass")
                    pass

    if stop:
        break


# // outputting the result:
string = ""
space = " "
for i in range(len(array)):
    if i == len(array)-1:
        space = ""
    string += (array[i] + space)
print(string)


# // number of comparisions in the first work of [i] for loop is 
