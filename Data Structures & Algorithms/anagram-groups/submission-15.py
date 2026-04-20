class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count the frequencies, return the sublists as tuples in list format

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # for all letters a-z lowercase
            for c in s:
                count[ord(c) - ord('a')] += 1 # count the frequency of characers 
            res[tuple(count)].append(s)
        
        return list(res.values())