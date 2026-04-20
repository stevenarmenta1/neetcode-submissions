class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intialize the results array with 1s
        # res[i] will be the size of all elements in nums, except nums[i]
        res = [1] * len(nums) # intialize results array to 1 values of size length of nums
        
        prefix = 1 # stores the product of all nums to left of i
        for i in range(len(nums)):
            res[i] = prefix # set res[i] to the product of all elements before i
            prefix *= nums[i] # up[date prefix by multiplying the current number
        postfix = 1 # store all products the right of i
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix # multiply current value by product of elements after i
            postfix *= nums[i] # update postfix by multiplying the current number
        return res