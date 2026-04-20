class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the frequencies of each characters in each string
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} 
        for i in range(len(s)):
             #count = [0] * 26 # for 26 letters in lowercase alphabet a - z
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT