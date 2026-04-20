class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: an array of strings strs
        # output: return the same list of strings with sublists of same anagrams. 
        # algorithm: Hash table! 

        finalList = defaultdict(list)

        for ministring in strs: 
            count = [0] * 26
            for letter in ministring: 
                count[ord(letter) - ord('a')] += 1
            finalList[tuple(count)].append(ministring)
        return list(finalList.values())