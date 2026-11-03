class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        res=51
        for i in range(n):
            if words[i]==target:
                res=min(abs(i-startIndex),abs(n-abs(i-startIndex)),res)
        if res==51:
            return -1
        return res       