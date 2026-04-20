class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store the num as a set, check the longest, also check the current length vs longest
        # create a numSet and store nums the input in it as a set
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num -1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest 
            