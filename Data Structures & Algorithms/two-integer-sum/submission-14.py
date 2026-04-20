class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # create a hash map to store value and indexes

        for i, n in enumerate(nums): 
            diff = target - n # computate the complement
            if diff in prevMap:
                return [prevMap[diff], i] # return the complements index and the current elements index
            # if not in prevMap we will add it to the prevMap
            prevMap[n] = i