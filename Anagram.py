# This method checks if two strings are anagrams.
# Anagram is a word or phrase formed by rearranging the letters of another
# or phrase, using all the original letters.

from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

print(anagram("abcd3", "3acdb"))

