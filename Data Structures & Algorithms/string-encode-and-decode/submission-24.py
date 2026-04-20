class Solution:

    def encode(self, strs: List[str]) -> str:
        # create a res string, add the list of strings.
        # Use a symbol such as # to seperate the individual strings
        # Do the length + # + actual string
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        # take the string and de code it back, after each #
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res