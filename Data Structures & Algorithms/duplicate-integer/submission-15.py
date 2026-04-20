class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        input: Given an array of integers called nums
        output: return true or false
        algorithm: make a hashset to store the array and check if duplicate appears
        '''
        saw = set()
        for num in nums: 
            if num in saw: 
                return True
            saw.add(num)
        return False