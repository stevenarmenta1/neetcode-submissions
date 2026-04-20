class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # convert to int
            # move i pointer past deliminator
            i = j + 1
            j = i + length # move j pointer to end of substring
            # convert substring into string to final list
            res.append(s[i:j])

            # update i pointer to j position to reset loop
            i = j
            
        return res

