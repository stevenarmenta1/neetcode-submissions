class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashmap to store the input array and perform checks
        hashset = []

        for num in nums:
            if num in hashset:
                return True # return true there are duplicates
            # appened or add the num to the hasset to continue on. 
            hashset.append(num)
        # if we make it out the loop with no duplicates we return false. 
        return False