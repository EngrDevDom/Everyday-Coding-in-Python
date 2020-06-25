
""" Challenge #1 : Shift_Code.py """

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", " "]

def get_data():
    word = input("Enter your message: ")
    word = word.lower()
    num = int(input("Enter a number (1-26): "))
    if num > 26 or num == 0:
        while num > 26 or num == 0:
            num = int(input("Out of range, please enter a number (1-26): "))
    data = (word,num)
    return(data)

def make_code(word,num):
    new_word = ""
    for x in word:
        y = alphabet.index(x)
        y += num
        if y > 26:
            y -= 27
        char = alphabet[y]
        new_word += char
    print("\nnew word =", new_word)
    print()

def decode(word,num):
    new_word = ""
    for x in word:
        y = alphabet.index(x)
        y -= num
        if y < 0:
            y += 27
        char = alphabet[y]
        new_word += char
    print("\nnew word =", new_word)
    print()

def main():
    again = True
    while again == True:
        print("1) Make a code")
        print("2) Decode a message")
        print("3) Quit")
        print()
        selection = int(input("Enter your selection: "))
        if selection == 1:
            (word,num) = get_data()
            make_code(word,num)
        elif selection == 2:
            (word,num) = get_data()
            decode(word,num)
        elif selection == 3:
            again = False
        else:
            print("Incorrect selection")

main()

