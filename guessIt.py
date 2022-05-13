import random

def play():

    print("*********************************")
    print("******Welcome to Guess It!*******")
    print("*********************************")

    secretNumber = random.randrange(1,101)
    totalAttempts = 0
    points = 1000

    print("What is the difficulty level?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Set the level: "))

    if(level == 1):
        totalAttempts = 20
    elif(level == 2):
        totalAttempts = 10
    else:
        totalAttempts = 5

    for round in range(1, totalAttempts + 1):
        print("Attempt {} of {}".format(round, totalAttempts))

        guess_str = input("Type a number between 1 and 100: ")
        print("You type " , guess_str)
        guess = int(guess_str)

        if(guess < 1 or guess > 100):
            print("You must type a number between 1 and 100!")
            continue

        gotItRight = guess == secretNumber
        bigger = guess > secretNumber
        smaller = guess < secretNumber

        if(gotItRight):
            print("You got it right and did {} points!".format(points))
            break
        else:
            if(bigger):
                print("You miss! Your guess was bigger than the secret number.")
            elif(smaller):
                print("You miss! Your guess was smaller than the secret number.")
            lost_points = abs(secretNumber - guess)
            points = points - lost_points

    print("Game over!")
    
if(__name__ == "__main__"):
    play()