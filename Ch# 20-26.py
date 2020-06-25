# Ch 20
firstname = input("Enter your first name: ")
print(len(firstname))

# Ch 21
firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
fullname = firstname + surname
print(fullname, ",", len(fullname))

# Ch 22
firstname = input("Enter first name in lower case: ")
surname = input("Enter surname in lower case: ")
fullname = firstname.title() + " " + surname.title()
print(fullname)

# Ch 23
str = input("Enter a nursery rhyme: ")
print("Length of str is", len(str))
startNum = int(input("Enter a starting number: "))
endNum = int(input("Enter a ending number: "))
print("Section is", str[startNum:endNum])

# Ch 24
word = input("Enter a word: ")
print(word.upper())

# Ch 25
firstname = input("Enter your first name: ")
if len(firstname) < 5:
    surname = input("Enter your surname: ")
    fullname = firstname + surname
    print(fullname.upper())
elif len(firstname) >= 5:
    print(firstname.lower())

# Ch 26
word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())
