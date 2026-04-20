class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use a prefix, postfix to output to the result output
        # store nums in a set, then iterate over the final output list
        # have to go right to left of i and left to right on second pass
        res = [1] * len(nums) # create an output list filled with ones for length of nums
        prefix = 1

        # first pass
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res