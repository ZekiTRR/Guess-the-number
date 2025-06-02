import random


print("Hi, want to play a game?")
print("Enter the minimum number")
min = int(input())
print("Enter the maximum number")
max = int(input())

if min > max:
    print("Invalid input")
    exit()
if min == max:
    print("Invalid input")
    exit()

#if max - min < 10:
#    print("Whoah that's a small range")
#    exit()

number = random.randint(min, max)

print("Okay, guess the number")
guess = int(input())


while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input())

print("You guessed it!")