# Problem 9 - Group Anagrams
# Group words that are anagrams of each other

def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

# Test it
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]