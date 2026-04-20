class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Algorithm: 2 pointer
        1. initialize 2 pointers
        2. check if at beginning and end are the same
        3. if .lower() versions of l and r are != return False
        4. update pointers to continue checking whole string
        5. must create an alphaNum def to check if pointers are alphaNum
        '''
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))