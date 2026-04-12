class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        limit = int(n**0.5) + 1
        mod = 10**9 + 7
        group = [[] for _ in range(limit)]
        
        for l, r, k, v in queries:
            if k >= limit:
                # Brute force
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % mod
            else:
                group[k].append((l, r, v))
        
        for k in range(1, limit):
            if not group[k]:
                continue
            mul_arr = [1] * (n + k + 1)
            for l, r, v in group[k]:
                # Find the last index in the range [l, r] that hits the step k
                last_idx = l + ((r - l) // k) * k
                mul_arr[l] = (mul_arr[l] * v) % mod
                
                # Inverse for modular division
                inv_v = pow(v, mod - 2, mod)
                mul_arr[last_idx + k] = (mul_arr[last_idx + k] * inv_v) % mod
            
            # Propagate the multipliers with step k
            for i in range(k, n):
                mul_arr[i] = (mul_arr[i] * mul_arr[i - k]) % mod
            
            # Apply to original nums
            for i in range(n):
                if mul_arr[i] != 1:
                    nums[i] = (nums[i] * mul_arr[i]) % mod
                    
        res = 0
        for val in nums:
            res ^= val
        return res