class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: given an integer array called nums, and a target number
        # output: return the indices of i and j the two numbers that add up to target number
        # algorithm: Hashmap - store indices that add together to get the target. 

        prevMap = {}

        for i, j in enumerate(nums):
            differance = target - j
            if differance in prevMap:
                return [prevMap[differance], i]


            prevMap[j] = i