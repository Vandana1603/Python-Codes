def is_armstrong(no):
    for d in str(no):
        digits = d
        power = len(digits)
        total = sum(int(d) ** power for d in digits)
    return total == no

number = int(input("Enter a number: "))
if is_armstrong(number):
    print("Armstrong Number")
else :
    print("Not Armstrong")
    