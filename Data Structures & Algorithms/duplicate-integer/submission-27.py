class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset 
        # perform checks to see if num is in hashmap
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False