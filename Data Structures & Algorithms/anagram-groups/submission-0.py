class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: an aray of strings strs 
        # output: return the list with all anagrams grouped into sublists. 
        # algorithm: Hash tabe
        #   pass through the strs array, if the letters are the same add them to a sublist. 

        finalList = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            finalList[tuple(count)].append(s)
        return list(finalList.values())