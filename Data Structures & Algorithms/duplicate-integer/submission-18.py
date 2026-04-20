class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashmap 
        # perform checks to see if num is in hashmap
        hashmap = []

        for num in nums:
            if num in hashmap:
                return True
            hashmap.append(num)
        return False