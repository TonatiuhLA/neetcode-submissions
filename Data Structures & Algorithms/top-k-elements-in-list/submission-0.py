class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n] += 1
        
        for key in frequency.keys():
            freq[frequency[key]].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        
        
