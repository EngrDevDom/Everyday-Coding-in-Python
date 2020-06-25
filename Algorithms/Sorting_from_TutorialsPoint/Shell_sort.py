# Shell_sort

"""
    Shell Sort involves sorting elements which are away from ech other.
    We sort a large sublist of a given list and go on reducing the size
    of the list until all elements are sorted. The below program finds
    the gap by equating it to half of the length of the list size and
    then starts sorting all elements in it. Then we keep resetting the
    gap until the entire list is sorted.
"""


def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            # Sort the sub list for this gap
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
            input_list[j] = temp

        # Reduce the gap for the next element
        gap = gap // 2


list = [19, 2, 31, 45, 30, 11, 121, 27]

shellSort(list)
print(list)