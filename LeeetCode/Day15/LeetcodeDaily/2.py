class Solution:
    def minPartitions(self, n: str) -> int:
        for d in "9876543210":
            if d in n:
                return int(d)               