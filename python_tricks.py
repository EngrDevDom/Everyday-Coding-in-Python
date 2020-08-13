''' 
    Interactive Shell 
    -> run this code in python -i filename.py
'''
def add(1,2):
    return first + second

'''
    Dict Comprehension
    -> Easier way to manipulate dict
'''
fruits = [
    {'name': 'apple', 'price': 20},
    {'name': 'avocado', 'price': 10},
    {'name': 'orange', 'price': 5}
]

print(
    { fruit['name']: fruit['price'] for fruit in fruits }
)


'''
    Lambda Function
'''
# Add func 1
def add(x, y):
    return x + y

# Add func 2
add2 = lambda x, y: x + y

# Generic Code
nums = [1, 2, 3]
def is_greater_than_one(x):
    return x > 1

more_than_one_nums = filter(is_greater_than_one, nums)
print(list(more_than_one_nums))

# Using lambda
more_than_one_nums = filter(lambda x: x > 1, [1, 2, 3])
print(list(more_than_one_nums))

