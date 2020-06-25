# More String Manipulation

# Ch 80
firstname = input("Enter your first name: ")
print(len(firstname))
surname = input("Enter your surname: ")
print(len(surname))
name = firstname + " " + surname
print(name)
print(len(name))

# Ch 81
subject = input("Enter your favorite school subject: ")
for letter in subject:
    print(letter, end="-")

# Ch 82
poem = "Oh, I wish I'd looked into your eyes."
print(poem)
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))
print(poem[start:end])

# Ch 83
msg = input("Enter a msg in uppercase: ")
tryAgain = False
while tryAgain == False:
    if msg.isupper():
        print("Thank you.")
        tryAgain = True
    else:
        print("Try again.")
        msg = input("Enter a message in uppercase: ")

# Ch 84
postcode = input("Enter your postcode: ")
start = postcode[0:2]
print(start.upper())

# Ch 85
name = input("Enter your name: ")
count = 0
name = name.lower()
for x in name:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count += 1
print("Vowels =", count)

# Ch 86
pswd1 = input("Enter a password: ")
pswd2 = input("Enter it again: ")
if pswd1 == pswd2:
    print("Thank you.")
elif pswd1.lower() == pswd2.lower():
    print("They must be in the same case.")
else:
    print("Incorrect.")

# Ch 87
word = input("Enter a word: ")
length = len(word)
num = 1
for x in word:
    position = length - num
    letter = word[position]
    print(letter)
    num += 1

