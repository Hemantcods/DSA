from functools import lru_cache
from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)

        @lru_cache(None)
        def solve(i, j):
            # all robots assigned
            if i == n:
                return 0

            # no factories left
            if j == m:
                return float('inf')

            res = float('inf')
            pos, cap = factory[j]

            dist = 0

            # try assigning k robots to this factory
            for k in range(cap + 1):
                if i + k > n:
                    break

                if k > 0:
                    dist += abs(robot[i + k - 1] - pos)

                res = min(res, dist + solve(i + k, j + 1))

            return res

        return solve(0, 0)