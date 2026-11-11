class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        eachOneCostTogether=cost1+cost2
        ans=0
        # buy the item with min cost to common
        common=min(need1,need2)
        if eachOneCostTogether>costBoth:
            ans+=costBoth*common
            need1-=common
            need2-=common
        else:
            ans+=(eachOneCostTogether)*common
            need1-=common
            need2-=common
        # finish the leftoff
        if need1:
            if cost1>costBoth:
                ans+=costBoth*need1
            else:
                ans+=cost1*need1
        if need2:
            if cost2>costBoth:
                ans+=costBoth*need2
            else:
                ans+=cost2*need2
        return ans
# Time Complexity : O(1)
# Space Complexity : O(1) 