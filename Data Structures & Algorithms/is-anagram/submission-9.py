class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the length if they are equal
        # if they are equal continue, else false
        # iterate through one string, add frequency counts to both 
        # return if the frequency counts are the same

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT