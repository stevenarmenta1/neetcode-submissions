class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialize an empty list
        res = []
        for s in strs: # iterate through each string in input array
            # convert the lngth of string to text, add a deliminator '#',
            # then add the actual string, this prevents ambiguity when decoding
            res.append(str(len(s)) + "#" + s)
        return "".join(res) # join all encoded pieces into a single string

    def decode(self, s: str) -> List[str]:
        res = [] # list to store decoded strings
        i = 0 # pointer used to walk through the encoded string
        # continue until we've processed the whole string
        while i < len(s):
            j = i # second pointer to find the deliminator "#"
            # move j forward untiul we find #, everything before reps a length
            while s[j] != "#":
                j += 1
            # convert the substring containing the length into an integer
            length = int(s[i:j])
            # move i past the # character
            i = j +1

            # calculate the end index of the actual string
            j = i + length

            # extract the string using the known length
            res.append(s[i:j])

            #move i to the start of the next encoded segment
            i = j
        # return the list of decoded strings
        return res

