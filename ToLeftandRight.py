# ToLeftandRight.py

nums = []
num_of_space = 0
current_num = int(input("Enter a number: "))
nums.append(current_num)
while True:
    num = int(input("Enter a number: "))
    if num > current_num:   num_of_space += 1
    elif num == current_num:    continue
    else:   num_of_space -= 1
    current_num = num
    nums.append(" " * num_of_space + str(num))
    if num_of_space == 0:   break
for num in nums:    print(num)
