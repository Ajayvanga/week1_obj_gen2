# Problem 4 - Valid Anagram
# Two words are anagrams if they use the same letters

def is_anagram(s, t):
    return sorted(s) == sorted(t)

# Test it
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False