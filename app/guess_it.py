import random


def play():

    print("*********************************")
    print("******Welcome to Guess It!*******")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    points = 1000

    total_attempts = choose_level()

    for round in range(1, total_attempts + 1):
        print("Attempt {} of {}".format(round, total_attempts))

        guess_str = input("Type a number between 1 and 100: ")
        print("You type ", guess_str)
        guess = int(guess_str)

        if(guess < 1 or guess > 100):
            print("You must type a number between 1 and 100!")
            continue

        got_it_right = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if(got_it_right):
            print("You got it right and did {} points!".format(points))
            break
        else:
            points = check_error(bigger, smaller, secret_number, guess, points)

    print("Game over!")


def choose_level():
    print("What is the difficulty level?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Set the level: "))

    total_attempts = 0

    if(level == 1):
        total_attempts = 20
    elif(level == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    return total_attempts


def check_error(bigger, smaller, secret_number, guess, points):
    if(bigger):
        print("You miss! Your guess was bigger than the secret number.")
    elif(smaller):
        print("You miss! Your guess was smaller than the secret number.")
        lost_points = abs(secret_number - guess)
        return points - lost_points


if(__name__ == "__main__"):
    play()
