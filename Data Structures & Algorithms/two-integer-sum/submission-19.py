class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in saved:
                return [saved[difference], i]
            saved[num] = i # save num and it's index in saved hash map
        
        return 