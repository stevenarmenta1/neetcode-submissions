class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input: given an int array
        # output: return true or false
        # Algorithm: hash set

        saw = set()
        
        for num in nums: 
            if num in saw:
                return True
            saw.add(num)
        return False