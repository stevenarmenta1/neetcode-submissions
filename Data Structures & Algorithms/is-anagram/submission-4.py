class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t) return False
        # create two hashmaps to store the letters in each string
        # iterate through the len of string s 
        # check if the count of each letter are the same in each string
        # return true if the counts are the same else return false

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

        # string s = apple
        # string t = banana sinc enot equal will return false at first if test
        # string s = ana
        # string t = ana pass first if test, for each letter in string s add count to countS