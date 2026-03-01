class Solution:
    def minPartitions(self, n: str) -> int:
        maxnum=0
        for i in n:
            maxnum=max(maxnum,int(i))
            if maxnum==9:
                return maxnum
        return maxnum                