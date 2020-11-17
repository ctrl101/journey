def collatz(number):
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 == 1:
            print(number += 1)

try:
    number = int(input("Enter number :"))
    while number > 1:
        collatz(number)
        number =  number // 2


except:
    print("must be an interger")

