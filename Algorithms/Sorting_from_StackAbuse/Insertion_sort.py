# Insertion Sort
# Time Complexity : O(n^2)

"""
    Like Selection Sort, this algorithm segments the list into sorted and
    unsorted parts. It iterates over the unsorted segment, and inserts the
    element being viewed into the correct position of the sorted list.
"""

def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


# Verify it works
random_list_of_nums = [9, 1, 15, 28, 6]
print("Original List: ", random_list_of_nums)
insertion_sort(random_list_of_nums)
print("Sorted List  : ", random_list_of_nums)