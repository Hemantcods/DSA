# TLE expexted 
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        def cost(i, j):
            arr = sorted(nums[i:j])
            median = arr[x // 2]
            return sum(abs(v - median) for v in nums[i:j])
        n = len(nums)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        def solve(i,rem):
            if rem==0:
                return 0
            if i>n-x:
                return float('inf')
            if dp[i][rem]!=float('inf'):
                return dp[i][rem]
            start=cost(i,i+x)+solve(i+x,rem-1)
            skip=solve(i+1,rem)
            dp[i][rem]=min(start,skip)
            return min(start,skip)
        return solve(0,k)
# Time Complexity O(nk*xlogx)
# Space Complexity O(nk+n+x)-> O(nk)


# Pre calculating the cost for all subarray

from sortedcontainers import SortedList
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [float('inf')] * (n - x + 1)

        left = SortedList()
        right = SortedList()

        lsum = 0
        rsum = 0

        # Precalculate first window
        for i in range(x):
            if len(left) <= len(right):
                left.add(nums[i])
                lsum += nums[i]
            else:
                right.add(nums[i])
                rsum += nums[i]

            if right and left[-1] > right[0]:
                a = left.pop(-1)
                b = right.pop(0)

                left.add(b)
                right.add(a)

                lsum += b - a
                rsum += a - b

        # Sliding window
        for i in range(n - x + 1):
            median = left[-1]

            cost[i] = (
                abs(len(left) * median - lsum)
                + abs(rsum - len(right) * median)
            )
            if i == n - x:
                break
            # Remove outgoing element
            elem = nums[i]
            if elem in left:
                left.remove(elem)
                lsum -= elem
            else:
                right.remove(elem)
                rsum -= elem
            # Add incoming element
            elem = nums[i + x]
            if not left or elem <= left[-1]:
                left.add(elem)
                lsum += elem
            else:
                right.add(elem)
                rsum += elem

            # Rebalance sizes
            while len(left) > len(right) + 1:
                elem = left.pop(-1)
                right.add(elem)
                lsum -= elem
                rsum += elem

            while len(left) < len(right):
                elem = right.pop(0)
                left.add(elem)
                rsum -= elem
                lsum += elem
        print(cost)
        # DP
        m = n - x
        prev = [0] * (n + 1)
        for rem in range(1, k + 1):
            curr = [float('inf')] * (n + 1)
            for i in range(m, -1, -1):
                start = cost[i] + prev[i + x]
                skip = curr[i + 1]
                curr[i] = min(start, skip)
            prev = curr
        return prev[0]
# Time Complexity O(xlogx+nlogn+nk)
# Space Complexity O(n+x)