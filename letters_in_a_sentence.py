# File  :   letters_in_a_sentence.py
# Desc  :   A program that counts the letters in a sentence.

def main():
    sentence = input("Enter a sentence: ")

    # count the number of words
    x = len(sentence.split())

    # count the number of white space
    y = x - 1

    z = x - y

    print("The number of letters in the sentence is:", z)

main()
