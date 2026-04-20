class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: given an integer array nums
        # output: return an array output where output[i] product of all elements. 
        # algorithm: brute force

        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res