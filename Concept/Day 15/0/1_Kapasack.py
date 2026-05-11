def knapsack_recurssive(weights,values,capacity,n):
    if n==0 or capacity==0:
        return 0
    if weights[n-1]>capacity:
        return knapsack_recurssive(weights,values,capacity,n-1)
    include=values[n-1] +knapsack_recurssive(weights,values,capacity-weights[n-1],n-1)
    exclude=knapsack_recurssive(weights,values,capacity,n-1)
    return max(include,exclude)
weights=[2,3,4,5]
values=[3,4,5,6]
capacity=5
print(knapsack_recurssive(weights,values,capacity,len(weights)))

def knapsack_dp(weights,values,capacity):
    n=len(weights)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                include=dp[i-1][w-weights[i-1]]+values[i-1]
                exclude=dp[i-1][w]
                dp[i][w]=max(include,exclude)
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
print(knapsack_dp(weights,values,capacity))
