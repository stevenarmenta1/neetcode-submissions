class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # second pass right to left
        postfix = 1
        for i in range(len(nums) -1, -1, -1): # second pass going right to left of i
            res[i] *= postfix # times output resolution string by postfix value
            postfix *= nums[i]
        
        return res