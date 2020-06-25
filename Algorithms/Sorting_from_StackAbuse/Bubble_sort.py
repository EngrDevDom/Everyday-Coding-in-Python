# Bubble Sort
# Time Complexity : O(n^2)

"""
    This simple sorting algorithm iterates over a list, comparing elements
    in pairs and swapping them until the larger elements "bubble up" to the
    end of the list, and the smaller elements stay at the "bottom".
"""

def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify if it works
random_list_of_nums = [5, 2, 1, 8, 4]
print("Original List: ", random_list_of_nums)
bubble_sort(random_list_of_nums)
print("Sorted List  : ", random_list_of_nums)