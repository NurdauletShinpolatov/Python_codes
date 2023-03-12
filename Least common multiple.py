a = int(input("a = "))
b = int(input("b = "))
factors_A = []
factors_B = []
factors = []
def factors(num):
    for i in range(2, num):
        while num%i==0:
            num = num/i
            factors_B.append(i)
factors(a)
factors_A = factors_B
factors_B = []
factors(b)

common_factors = []
lcm = 1
for j in factors_A:
    print("j =", j)
    notcommon = True
    for k in factors_B:
        if j==k:
            notcommon = False
            print("k =", k)
            common_factors.append(j)
            lcm *= j
    if notcommon == True:
        lcm *= j
for m in factors_B:
    notcommon = True
    for n in factors_A:
        if n==m:
            notcommon = False
    if notcommon == True:
        lcm *= m
print(lcm)

