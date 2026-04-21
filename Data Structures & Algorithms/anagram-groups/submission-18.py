class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given array of strings, group them into sub lists.
        # sublist are mini groups of characters that are the same but order can be different.
        # Use a character count to count

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # letters in alphabet a-z
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())