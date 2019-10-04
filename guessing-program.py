#!user/bin/env python3

# Created by: RJ Fromm
# Created on: September 2019
# This program is a number guessing game

import random


def main():

    random_number = random.randint(1, 100+1)

    secret_number = int(input("Guess my secret number : "))

    if secret_number == random_number:
        print("WOW! YOU GUESSED THE RANDOM NUMBER! WHAT DO YOU WANT? A MEDAL")

    else:
        print("The random number was", (random_number))


if __name__ == "__main__":
    main()
