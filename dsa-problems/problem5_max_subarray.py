# Problem 5 - Maximum Subarray
# Find the largest sum of a continuous subarray

def max_subarray(nums):
    max_sum = nums[0]
    current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum

# Test it
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray([1, 2, 3, 4, 5]))                    # 15