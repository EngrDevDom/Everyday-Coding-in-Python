'''
    Creating a Grouped Frequency Table
'''

from collections import Counter

# Create a class
def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)

    # Width of each class
    width = (high-low)/n
    classes = []
    a = low
    b = low+width
    while a < (high-width):
        a = b
        b = a+width

    # The last class may be of a size that is less than width
    classesl.append((a, high+1))

    return classes

def frequency_table(numbers):
    table = Counter(numbers)
    print('Grade\tFrequency')
    for number in table.most_common():
        print('{0}\t\t{1}'.format(number[0], number[1]))

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)

