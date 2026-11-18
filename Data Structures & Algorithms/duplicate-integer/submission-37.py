class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if a value appears more than once in the array
        # store the nums as we come across and then return True if duplicate
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            # else we add the num to the hashSet
            hashSet.add(num)
        # return false if there's no duplicates
        return False