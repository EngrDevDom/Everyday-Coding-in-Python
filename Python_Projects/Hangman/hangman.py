# Simple Hangman Game

# import Python functions
from random import *

# Provide score variables
player_score = 0
computer_score = 0

# Involve ASCII art of the game's stages, printed out every turn
def hangedman(hangman):
    graphic = [
        """
            +-------+
            |
            |
            |
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       0
            |
            |
            |
        ===============
        """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      / \
        |
    ===============
        """ ]

    print(graphic[hangman])
    return

# The actual game starts here
def start():
    print("Let's play a game of Linux Hangman.")
    while game():
        pass
    scores()

# The game rules are decided here, as well as the setup for the word and keeping track of tries and incorrect answers
def game():
    dictionary = ["gnu", "kernel", "linux", "mageia", "penguin", "ubuntu"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length*["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    # Each round of the game is played here, asking for an input, then telling you if you were correct or not.
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You've already picked", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry", letter, "isn't what were looking for.")
                else:
                    print("Congratulations", letter, "is correct.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Choose another.")

        hangedman(letters_wrong)
        print("".join(clue))
        print("Guesses:", letters_tried)

        # After each round, the code checks if you've won or lost yet
        if letters_wrong == tries:
            print("Game Over.")
            print("The word was", word)
            computer_score += 1
            break
        if ("".join(clue) == word):
            print("You win!")
            print("The word was", word)
            player_score += 1
            break
    return play_again()

# The human input for the game takes the letter and turns it into something the can use
def guess_letter():
    print()
    letter = print("Take a guess at our mystery word:")
    letter.strip()
    letter.lower()
    print()
    return letter

# Allows you to select whether or not you wish to play again
def play_again():
    answer = print("Would you like to play again? y/n:")
    if answer in ("y", "Y", "yes", "YES", "Of course!"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")

# Upon quitting the game, scores are given for the duration of the play session
def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

if __name__ == '__main__':
    start()

