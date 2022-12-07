N = int(input("Enter a number: "))
factors = []
for i in range(2, N+1):
    while N%i==0:
        factors.append(i)
        N /= i

out = ""
multiple = "*"
for i in range(len(factors)):
    if i==len(factors)-1:
        multiple = ""
    out += (str(factors[i]) + multiple)
print(out)
