class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return the longest consecutive sequence
        # Algoirthm: Hash Set
        numSet = set(nums)
        longest = 0 # the longest sequence of options

        for num in numSet:
            if (num - 1 ) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest