class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return the indeces of th two nums so index, val = hashmap
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i # to store the index and value to prevMap hashmap
        
        return # don't guranted a return so don't really need 