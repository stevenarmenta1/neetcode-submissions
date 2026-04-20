class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given int array nums and target
        # create hashmap of indice and value

        hashmap = {} # create hashmap to store indices and values

        for i, n in enumerate(nums): # create a for loop for the indices using enumerate 
            # difference = target - n
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
            