class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] # encode the string with the # with length in front and complete string after #
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # initialize result list and first pointer i

        while i < len(s):
            j = i # initialize j 2nd pointer to i position
            # move j 2nd pointer to decromentor #
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) 
            # update the i pointer to 1 position after #
            i = j + 1 
            j = length + i # move j pointer to end of the substring
            res.append(s[i:j])
            i = j
        
        return res

            

