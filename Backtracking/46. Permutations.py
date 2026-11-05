class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        def backtrack(ans,later=[]):
            if len(later)==n:
                ans.append(later.copy())
            else:
                for i in range(n):
                    if nums[i] in later:
                        continue
                    later.append(nums[i])
                    backtrack(ans,later)
                    later.pop()
        backtrack(ans,[])
        return ans
