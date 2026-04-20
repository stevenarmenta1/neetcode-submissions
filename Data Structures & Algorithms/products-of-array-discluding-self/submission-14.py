class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' two passes with prefix, postfix
            can be solved in O(n) space and O(n) time complexity
            use the output as memory to update the product values
        '''
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # second pass prefix = 1
        # go right to left
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
