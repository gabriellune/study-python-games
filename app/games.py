import app.hangman as hangman
import app.guess_it as guess_it


def choose_game():

    print("***********************************")
    print("*********Choose your game!*********")
    print("***********************************")

    print("(1) Hangman (2) Guess It")

    game = int(input("Which game?"))

    if(game == 1):
        print("Playing Hangman")
        hangman.play()
    elif(game == 2):
        print("Playing Guess It")
        guess_it.play()


if(__name__ == "__main__"):
    choose_game()
