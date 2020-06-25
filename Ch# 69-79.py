# Tuples, Lists and Dictionaries

# Ch 69
countries = ["philippines", "russia", "taiwan", "korea", "japan"]
print(countries)
choice =input("\nEnter your choice: ")
print(choice, "has index number", countries.index(choice))

# Ch 70
countries = ["philippines", "russia", "taiwan", "korea", "japan"]
print(countries)
choice =input("\nEnter your choice: ")
print(choice, "has index number", countries.index(choice))
num = int(input("\nEnter a number between 0 and 4: "))
print(num, "is country", countries[num])

# Ch 71
sports_list = ["basketball", "table tennis", "chess", "running"]
sports_list.append(input("What is your favorite sport?: "))
sports_list.sort()
print(sports_list)

# Ch 72
subject_list = ["maths", "english", "computing", "history", "science", "spanish"]
print(subject_list)
dislike = input("Which of these subjects do you dislike? ")
getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)

# Ch 73
food_dictionary = {}
food1 = input("Enter a food you like: ")
food_dictionary[1] = food1
food2 = input("Enter a food you like: ")
food_dictionary[2] = food2
food3 = input("Enter a food you like: ")
food_dictionary[3] = food3
food4 = input("Enter a food you like: ")
food_dictionary[4] = food4
print(food_dictionary)
dislike = int(input("Which of these do you want to get rid of? "))
del food_dictionary[dislike]
print(sorted(food_dictionary.values()))

# Ch 74
colours = ["red", "blue", "green", "black", "white", "pink", "grey", "purple", "yellow", "brown"]
start = int(input("Enter a starting number (0-4): "))
end = int(input("Enter an end number (5-9): "))
print(colours[start:end])

# Ch 75
nums = [123, 345, 234, 765]
for i in nums:
    print(i)
selection = int(input("Enter a number from the list: "))
if selection in nums:
    print(selection, "is in position", nums.index(selection))
else:
    print("That is not in the list.")

# Ch 76
name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1, name2, name3]
another = input("Do you want to invite another (y/n): ")
while another == "y":
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n): ")
print("\nYou have", len(party), "people coming to your party.")

# Ch 77
name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1, name2, name3]
another = input("Do you want to invite another (y/n): ")
while another == "y":
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n): ")
print("\nYou have", len(party), "people coming to your party.")
print(party)
selection = input("Enter one of the names: ")
print(selection, "is in position", party.index(selection), "on the list.")
stillcome = input("Do you want them to come? (y/n): ")
if stillcome == "n":
    party.remove(selection)
print(party)

# Ch 78
tv = ["Task Master", "Top Gear", "The Big Bang Theory", "Silicon Valley"]
for i in tv:
    print(i)
print()
newtv = input("Enter another TV show: ")
position = int(input("Enter a number between 0 and 3: "))
tv.insert(position, newtv)
print()
for i in tv:
    print(i)

# Ch 79
nums = []
count = 0
while count < 3:
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    count += 1
lastnum = input("Do you want the last number saved (y/n)? : ")
if lastnum == "n":
    nums.remove(num)
print(nums)

