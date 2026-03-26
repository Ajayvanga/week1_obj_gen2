# Problem 10 - Palindrome Check
# A word that reads the same forwards and backwards

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test it
print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("madam"))     # True