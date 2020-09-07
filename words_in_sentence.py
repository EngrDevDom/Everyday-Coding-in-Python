# File  :   words_in_sentence.py
# Desc  :   A program that counts the number of words in a sentence.

def main():
    sentence = input("Enter a sentence: ")
    words = len(sentence.split())
    print("The number of words in the sentence is: ", words)

main()
