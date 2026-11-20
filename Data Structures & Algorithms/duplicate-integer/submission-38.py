class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        saved = set()
        for num in nums:
            if num in saved:
                return True
            saved.add(num)
        return False