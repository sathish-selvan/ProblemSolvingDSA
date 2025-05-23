from collections import defaultdict

import heapq

nums = [1,1,1,2,2,3]

k = 1

def frequent_elements(nums: list , k:int):
    
    h = defaultdict(int)
    for ele in nums:
        h[ele] += 1
    res = []
    
    for num, freq in h.items():
        heapq.heappush(res, (freq, num))
        if len(res) > k:
            heapq.heappop(res)
            
    return [num for freq, num in res]
    
print(frequent_elements(nums, k))
    
    