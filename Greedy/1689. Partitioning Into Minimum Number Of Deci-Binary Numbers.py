# Approach 1: Track the maximum digit
class Solution:
    def minPartitions(self, n: str) -> int:
        maxnum=0
        for i in n:
            maxnum=max(maxnum,int(i))
            if maxnum==9:
                return maxnum
        return maxnum                


# Approach 2: Search digits from 9 down to 0
class Solution:
    def minPartitions(self, n: str) -> int:
        for d in "9876543210":
            if d in n:
                return int(d)               


# Approach 3: Return the maximum digit
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))             
