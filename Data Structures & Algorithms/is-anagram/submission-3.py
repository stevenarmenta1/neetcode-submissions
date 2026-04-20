class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given two strings, return true if two strings are anagrams of eachother otherwise return false

        # 1 if the two aren't the same length, return false
        # 2 store both the strings in hashmaps, then compare whether they contain the same letters

        if len(s) != len(t):
            return False
        
        lettersInS, lettersInT = {}, {}
        
        # if the two string lengths are the same, we can iterate and add to both maps for the length of one of 
        # the strings
        for letter in range(len(s)):
            lettersInS[s[letter]] = 1 + lettersInS.get(s[letter], 0)
            lettersInT[t[letter]] = 1 + lettersInT.get(t[letter], 0)
        
        return lettersInS == lettersInT