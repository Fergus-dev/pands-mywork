import random

x = random.randint(1, 100)

guess = int(input("Enter a number between 1 and 100: "))

while guess != x:
    if guess < x:
        guess = int(input("Too low, try again: "))
    else:
        guess = int(input("Too high, try again: "))

print("Well done! You guessed the number correctly.")