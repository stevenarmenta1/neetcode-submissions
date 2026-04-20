class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashlist = set()

        for n in nums:
            if n in hashlist:
                return True
            hashlist.add(n)
        return False