class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' return True if they are anagrams of each other
            this means they return true if same letters
            I could make 2 hashMaps and store the values and 
            check if they are the same 
            
            #1 check if they are the same length, else False'''
        if len(s) != len(t):
            return False
        # 2 store 2 counts for s and T
        countS, countT = {}, {}
        # 3 get the count of each time a character appears for both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # return true if their counts of each characters are the same
        if countS == countT:
            return True
        return False
    