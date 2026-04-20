class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count frequencies, of each string
        # group frequencies together and return the string values
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # append s to result strins
        
        return list(res.values())  