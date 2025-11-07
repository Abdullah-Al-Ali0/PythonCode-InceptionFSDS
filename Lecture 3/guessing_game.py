import random

jackpot_num = random.randint(1, 100)

guess_num = int(input("Guess a Number: "))

counter = 1

while guess_num != jackpot_num:

    if guess_num < jackpot_num:
        print("Wrong! guess a higher number.")

    else:
        print("Wrong! guess a lower number.")

    guess_num = int(input("Guess the Number again: "))
    counter += 1


else:
    print("Correct!")
    print("You guessed the number in", counter, "tries.")