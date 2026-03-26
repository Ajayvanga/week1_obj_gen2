# Problem 7 - Merge Two Sorted Arrays

def merge_sorted(a, b):
    return sorted(a + b)

# Test it
print(merge_sorted([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
print(merge_sorted([10, 20], [5, 15, 25]))  # [5, 10, 15, 20, 25]