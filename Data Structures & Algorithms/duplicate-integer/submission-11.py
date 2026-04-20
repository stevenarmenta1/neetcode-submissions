class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset algorithm
        # 1 Create a hashset hashset = set()
        # 2 for each number in the int array nums
        # return true if num is in the stored hash set, else we'll loop through and add the num to the array. 
        # 3 return false if we make it through the whole array and no duplicates. 
        
        hashset = set()
        for num in nums: 
            if num in hashset:
                return True
            hashset.add(num)
        return False
        
