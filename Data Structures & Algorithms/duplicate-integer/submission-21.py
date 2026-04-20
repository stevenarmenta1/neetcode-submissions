class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hashset to store numbers seen
        # iterate over the array and return true if any are duplicates
        # return false and add to hashset if not in the hashset already

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False