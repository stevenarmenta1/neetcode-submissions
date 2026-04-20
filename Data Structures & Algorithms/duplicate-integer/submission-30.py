class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevSeen = set()
        for n in nums:
            if n in prevSeen:
                return True
            prevSeen.add(n)
    
        return False
