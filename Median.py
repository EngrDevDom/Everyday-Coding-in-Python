num_list = [21, 13, 19, 3, 11, 5]

# Sort the list
num_list.sort()

# Finding the position of the median
if len(num_list)%2 == 0:
    first_median = num_list[len(num_list) // 2]
    second_median = num_list[len(num_list) // 2 - 1]
    median = (first_median + second_median) / 2
else:
    median = num_list[len(num_list) // 2]

print(num_list)
print("Median of above list is : " + str(median))