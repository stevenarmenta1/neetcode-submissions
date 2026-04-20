class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hashset to store numbers and check if in list as we iterate through list
        # create hash set
        # for n in nums:
        # if n in hashset return true
        # otherwise add n to hashset 
        # return false if iterate through the whole list and no duplicate

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False