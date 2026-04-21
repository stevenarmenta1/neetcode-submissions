class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          # create a count hashmap, and frequency for each. 
          # after getting each frequency of number 
          # gor right to left to get the most frequent of k. 

        count = {}
        freq = [[] for i in range(len(nums) + 1)] # off by 1 errors

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = [] # final result output array
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]: 
                res.append(num)
                if len(res) == k:
                    return res