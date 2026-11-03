from collections import defaultdict
import bisect
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        m = len(nums)
        res=[]
        pos=defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        for idx in queries:
            num = nums[idx]
            arr=pos[num]
            if (len(arr)==1):
                res.append(-1)
                continue
            # apply binary search    
            ans = float('inf')
            i = bisect.bisect_left(arr, idx)

            left = arr[i-1] if i-1 >= 0 else arr[-1]
            d1 = abs(idx - left)
            ans = min(ans, min(d1, m - d1))
            
            # Check right neighbor
            # RIGHT (skip same index)
            if i < len(arr) and arr[i] == idx:
                right = arr[i+1] if i+1 < len(arr) else arr[0]
            else:
                right = arr[i] if i < len(arr) else arr[0]
            d2 = abs(idx - right)
            ans = min(ans, min(d2, m - d2))
            res.append(ans)
        return res