class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: given an array of strings strs
        # output: group all anagrams together into sublist and return the list. 
        # Algorithm: Hash table

        result = defaultdict(list)
        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())