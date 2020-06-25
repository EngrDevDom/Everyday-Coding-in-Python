# 2D Lists and Dictionaries

# Ch 96
list = [ [2,5,8], [3,7,4], [1,6,9],[4,2,0] ]
print(list)


# Ch 97
list = [ [2,5,8], [3,7,4], [1,6,9],[4,2,0] ]
row = int(input("Select a row: "))
col = int(input("Select a column: "))
print(list[row][col])


# Ch 98
list = [ [2,5,8], [3,7,4], [1,6,9],[4,2,0] ]
row = int(input("Select a row: "))
print(list[row])
new_value = int(input("Enter a new number: "))
list[row].append(new_value)
print(list[row])


# Ch 99
list = [ [2,5,8], [3,7,4], [1,6,9],[4,2,0] ]
row = int(input("Select a row: "))
print(list[row])
col = int(input("Select a column: "))
print(list[row][col])
change = input("Do you want to change the value? (y/n) ")
if change == "y":
    new_value = int(input("Enter a new value: "))
    list[row][col] = new_value
print(list[row])


# Ch 100
sales = { "John": { "N":3056, "S":8463, "E":8441, "W":2694 },
          "Tom":  { "N":4832, "S":6786, "E":4737, "W":3612 },
          "Anne": { "N":5239, "S":4802, "E":5820, "W":1859 },
          "Fiona":{ "N":3904, "S":3645, "E":8821, "W":2451 } }

# Ch 101
sales = { "John": { "N":3056, "S":8463, "E":8441, "W":2694 },
          "Tom":  { "N":4832, "S":6786, "E":4737, "W":3612 },
          "Anne": { "N":5239, "S":4802, "E":5820, "W":1859 },
          "Fiona":{ "N":3904, "S":3645, "E":8821, "W":2451 } }

person = input("Enter sales person's name: ")
region = input("Select region: ")
print(sales[person][region])
new_data = int(input("Enter new data: "))
sales[person][region] = new_data
print(sales[person])


# Ch 102
list = {}
for i in range(4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age":age, "Shoe size":shoe}

ask = input("Enter a name: ")
print(list[ask])


# Ch 103
list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age":age, "Shoe size":shoe}

for name in list:
    print((name), list[name]["Age"])


# Ch 104
list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age":age, "Shoe size":shoe}

get_rid = input("Who do you want to remove from the list? ")
del list[get_rid]

for name in list:
    print((name), list[name]["Age"],list[name]["Shoe size"])

