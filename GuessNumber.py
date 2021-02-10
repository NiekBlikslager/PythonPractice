import random


def check_integer(user_input):
    if user_input.isdigit():
        return True
    print("That's not an integer, please provide an integer")
    return False


def guess():
    while True:
        inp = input("What is your guess? ")
        if check_integer(inp):
            return int(inp)


def evaluate(num, count, number):
    if num == number:
        print("Correct!")
        return 1
    elif count == 1:
        high_low(num, number)
        return 0
    elif count == 2:
        multiple(number)
        return 0
    else:
        difference(num, number)
        return 0


def high_low(num, number):
    if num > number:
        print("Too high!")
    elif num < number:
        print("Too low!")


def difference(num, number):
    print("The difference between the number and your guess is :", abs(num - number))


def multiple(number):
    a = b = c = 0
    if number % 2 == 0:
        a = 1
    if number % 3 == 0:
        b = 1
    if number % 5 == 0:
        c = 1
    if a + b + c == 0:
        print("The number is not a multiple of 2, 3, or 5")
    else:
        print("The number is a multiple of:", a*"2", b*"3", c*"5")


print("Create a range from which 1 number will picked")
while True:
    a = 1
    b = input("The range is from 1 up to which number?: ")
    if check_integer(b):
        b = int(b)
        break

number = random.randint(1, int(b))
correct = 0
n_guesses = 0
print("Try to guess the number between", a, "and", b)

while correct == 0:
    ans = guess()
    n_guesses += 1
    correct = evaluate(ans, n_guesses, number)

print("You guessed", n_guesses, "times!")
