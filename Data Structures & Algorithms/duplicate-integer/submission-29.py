class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored = set()
        for num in nums:
            if num in stored:
                return True # return true that there is a duplicate
            stored.add(num) # add number to the hashmap if not in stored 
        
        return False # return False there are no duplicates found


    ''' dry run walk through
        ex 1 nums = [ 1, 2, 3, 3]
        for 1 in nums:
            is 1 stored in stored?
                return true - won't exectue
            no - add to the stored list
        now it will go for the next number2 ..

    '''