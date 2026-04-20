class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []  # initialize an empty list to store encoded pieces

        for s in strs:  # iterate through each string in the input list
            # convert the length of the string to text,
            # add a delimiter (#),
            # then add the actual string
            # this prevents ambiguity when decoding
            res.append(str(len(s)) + "#" + s)

        # join all encoded pieces into a single string
        return "".join(res)
            
    def decode(self, s: str) -> List[str]:
        res = []  # list to store decoded strings
        i = 0     # pointer used to walk through the encoded string

        # continue until we've processed the entire string
        while i < len(s):
            j = i  # second pointer to find the delimiter '#'

            # move j forward until we find '#'
            # everything before '#' represents the length
            while s[j] != "#":
                j += 1

            # convert the substring containing the length into an integer
            length = int(s[i:j])

            # move i past the '#' character
            i = j + 1

            # calculate the end index of the actual string
            j = i + length

            # extract the string using the known length
            res.append(s[i:j])

            # move i to the start of the next encoded segment
            i = j

        # return the list of decoded strings
        return res
