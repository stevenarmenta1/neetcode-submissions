class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hashmap to store the array
        # if it's in the array, return True, else return False no duplicates

        hashset = set()
        for n in nums:
            if n in hashset:
                return True # true there is a duplicate
            hashset.add(n) # else we add to the hashset
        return False


    # example input = [1,2,3, 3]