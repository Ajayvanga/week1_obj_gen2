# Problem 2 - Contains Duplicate
# Check if any number appears more than once

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Test it
print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False