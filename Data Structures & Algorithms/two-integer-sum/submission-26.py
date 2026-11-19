class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force check each next to each other if they add to the the target
        # hashMap and store the nums array and check if target - num — that value is stored in the hashMap

        prevSeen = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in prevSeen:
                return [prevSeen[value], i]
            # else we add it to prevSeen
            prevSeen[num] = i