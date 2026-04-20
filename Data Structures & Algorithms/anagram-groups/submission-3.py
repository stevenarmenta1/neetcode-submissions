class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: An array of strings
        # output: group all anagrams together into sublist and return list
        # Algorithm: Hash table

        finalList = defaultdict(list)

        for s in strs: 
            count = 26 * [0]
            for letter in s:
                count[ord(letter) - ord('a')] += 1 
            finalList[tuple(count)].append(s)
        return list(finalList.values())