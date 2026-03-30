class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def solve(curr):
            if len(curr) == n:
                res.append(curr)
                return
            
            for char in ["a", "b", "c"]:
                if curr and curr[-1] == char:
                    continue
                solve(curr + char)

        res = []
        solve("")

        if len(res) < k:
            return ""
        return res[k-1]
