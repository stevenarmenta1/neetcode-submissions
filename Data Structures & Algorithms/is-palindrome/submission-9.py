class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' return true if palindrome, return false if not
            can use two pointers for beginning and end
            need to create an alphaNum helper function to check against, 
            move pointers if they are the same, else return False if they differ
            1. initialize two pointers
        '''
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r -1
        return True

    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))