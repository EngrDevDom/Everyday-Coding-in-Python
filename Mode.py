import collections

# List of elements to calculate mode
num_list = [21, 13, 19, 13, 19, 13, 1, 23, 125, 2, 13, 1, 1, 12, 1, 1]

# Print the list
print(num_list)

# Calculate the frequency of each item
data = collections.Counter(num_list)
data_list = dict(data)

# Print the items with frequency
print(data_list)

# Find the highest frequency
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(num_list):
   print("No mode in the list")
else:
   print("The Mode of the list is : " + ', '.join(map(str, mode_val)))