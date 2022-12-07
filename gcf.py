a = int(input("a = "))
b = int(input("b = "))
##if b>a: # swapping variables if b is greater 
##    a = a+b 
##    b = a-b 
##    a = a-b 

if b>a: # swapping variables if b is greater 
    a, b = b, a
    
rem = a%b # reminder 
num1 = b 
while rem!=0:
    num2 = rem
    rem = num1%rem
    num1 = num2
print(num1)
