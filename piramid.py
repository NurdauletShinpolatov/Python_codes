
sym = input("Enter a symbol: ") #// symbol which will be used
n = int(input("Enter a number: ")) #// max number of symbols
while n%2!=1: #// to get an odd number
    n = int(input("Enter a number: "))
    #max_spaces = (n-1)/2
max_spaces = int((n-1)/2) #// spaces from the beginning to the symbol
sym2 = ""
num = 0
for i in range(max_spaces):
    if i == 1:
        sym2 = sym
        num = 1
    print(" "*(max_spaces-i) + sym + " "*num + sym2)
    num += 2
print(sym*n)
