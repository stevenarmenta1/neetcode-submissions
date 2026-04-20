class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # step 1 initialize an empty hash set to store as we pass
        alreadySeen = set()
        # iterate through each number in the array
        for number in nums:
            # if number is in already seen, return true
            if number in alreadySeen:
                return True
            # add number to alreadySeen
            alreadySeen.add(number)
        # return false otherwise
        return False