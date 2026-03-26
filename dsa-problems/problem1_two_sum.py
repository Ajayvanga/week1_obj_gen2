# Problem 1 - Two Sum
# Find two numbers that add up to the target

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Test it
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]