class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return the indices of the two numbers in nums that = target

        prevMap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[num] = i
        
        return 