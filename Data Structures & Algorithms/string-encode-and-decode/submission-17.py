class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # first we encode the string, then we can decode it 
        # by doing the length to an int, then use pointers for the substring to decode
        # initialize a pointer at the beginning of s string

        res, i = [], 0
        while i < len(s):
            j = i
            # increment j if it's not currently on the # tag decrementor
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            res.append(s[i:j])
            i = j

        return res
            