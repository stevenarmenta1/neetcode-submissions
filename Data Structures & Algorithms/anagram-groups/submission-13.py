class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagrams into sublist
        # match for a frequency counter
        # all lower case so use [0] * 26 to cover a-z lowercase
        ''' 
        plan: 
        1 create a frequency counter to count, 
        2 for each string in strings input if they have the same
        3 i will add them to their designated group
        4 return the tuple list '''
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())