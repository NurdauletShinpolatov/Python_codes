maximum = int(input("Enter maximum number in range I should find your number: "))
guess = maximum // 2
print("\nmy guess =", guess)
feedback = input("Is my guess greater or less or equal to your number? \n(+;-;=): ")
minimum = 0
while feedback != "=":
    if feedback == "-":
        minimum = guess
        guess += (maximum - minimum)//2
    elif feedback == "+":
        maximum = guess
        guess -= (maximum - minimum)//2
    print("\nmy guess =", guess)
    feedback = input("Is my guess greater or less or equal to your number? \n(+;-;=)")
print("Wow. I found your number )))")
