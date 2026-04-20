class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Alogrithm: Two Pointers
        1. Initialize two pointers
        2. If the sum of the two pointers is greater than the target, r -= 1
            * if the sum is smaller than the target, l += 1
            * if the sum == target, return the indices l + 1, r + 1 since 1-indexed
        '''
        res = []
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target: 
                l += 1
            else:
                return [l + 1, r + 1]
                