class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: given two strings s and t, they can be anagrams of each other. 
        # output: return True or False
        # Algorithm: Check if they are equal we can use a Hashmap. 

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT