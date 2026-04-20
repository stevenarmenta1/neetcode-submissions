class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understand: return indices if i and j that make up the target
        #   there is 1 solution guranteed, i and j cannot be the same index. 
        # match: can create a hashmap / dictionary to store values and indices, 
        #   can iterate through the list check if in hashmap, if not add, continue throughout array 
        # plan: the plan is to create hashmap, for loop for both i index and n number/value
        #   create diff variable of target - n and look to see if have that val in pMap
        #   if the value is then we will return index of value in pMap and the current index
        #   if not then we can add the value n and index i to the pMap stored map to use for the next iteration.
        # implement: Coded the solution
        # Review: edge cases, test 1: [4 5 5 6] target = 10
        #   4 goes in for loop first, 10 - 4 assigns 6 as diff, 6 not in pMap so does not execute return statement
        #   stores 4 the pMap with the index 0 and goes to 5 next. 
        #   negative numbers? Yes they can go through and be stored. [ -1 1 3 5 ] diff = 4 - -1 = 5 
        # evalute: 
        #   time complexity: one pass through going through the list. O(n)
        #   space complexity: O(n) as it may take the whole array to be stored to find the pair

        pMap = {} 

        for i, n in enumerate(nums):
            diff =  target - n
            if diff in pMap:
                return [pMap[diff], i]
            pMap[n] = i
        return 