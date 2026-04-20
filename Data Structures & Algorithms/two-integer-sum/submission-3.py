class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: given an array of int nums, and target
        # output: return the indices such that they add to target
        # algorithm: Hashmap one pass

        prevMap = {}

        for i,n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i 