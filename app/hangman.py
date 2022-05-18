import random


def play():

    print("*********************************")
    print("******Welcome to Hangman!********")
    print("*********************************")

    secret_word = load_secret_word()

    correct_letters = initialize_correct_letters(secret_word)

    print(correct_letters)

    hanged = False
    got_it_right = False
    mistakes = 0

    while not hanged and not got_it_right:

        guess = input("Which letter?").strip().upper()

        if guess in secret_word:
            register_correct_guess(secret_word, guess, correct_letters)
        else:
            mistakes += 1
            drawing_the_hanging(mistakes)

        hanged = mistakes == 7
        got_it_right = "_" not in correct_letters
        print(correct_letters)

    if got_it_right:
        print("Congratulations.You win!")
    else:
        print("You lose!")
        print("The word was {}:".format(secret_word))


def load_secret_word():
    archive = open("app/words.txt", "r")
    words = []

    for line in archive:
        line = line.strip()
        words.append(line)

    archive.close()

    word_index = random.randrange(0, len(words))

    secret_word = words[word_index].upper()

    return secret_word


def initialize_correct_letters(secret_word):
    return ["_" for letter in secret_word]


def register_correct_guess(secret_word, guess, correct_letters):
    index = 0
    for letter in secret_word:
        if guess == letter:
            correct_letters[index] = letter
            index += 1


def drawing_the_hanging(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
