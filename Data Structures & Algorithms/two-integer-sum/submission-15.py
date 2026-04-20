class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # to return indices you can store vals and indexes with hashmap 
        prevMap = {} 

        for num, i in enumerate(nums):
            diff = target - i
            if diff in prevMap:
                return [prevMap[diff], num]
            prevMap[i] = num
        