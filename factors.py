number = int(input("Enter a integer: "))
for divisor in range(1, number + 1):
    if number % divisor == 0:
        print("{} is a divisor of {}".format(divisor, number))
