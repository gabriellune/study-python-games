import hangman
import guessIt

def chooseGame():
    
    print("***********************************")
    print("*********Choose your game!*********")
    print("***********************************")

    print("(1) Hangman (2) Guess It")

    game = int(input("Which game?"))

    if(game ==1):
        print("Playing Hangman")
        hangman.play()
    elif(game == 2):
        print("Playing Guess It")
        guessIt.play()
        
if(__name__ == "__main__"):
    chooseGame()