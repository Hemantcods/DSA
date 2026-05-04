def fractional_knapsack(item_wt,price,capacity):
    n=len(item_wt)
    items=[(price[i],item_wt[i],price[i]/item_wt[i]) for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if items[i][2]<items[j][2]:
                items[i],items[j]=items[j],items[i]
    print(items)
    profit=0.0
    for price,item_wt,perKgPrice in items:
        if capacity>=item_wt:
            profit+=price
            capacity-=item_wt
        else:
            profit+=perKgPrice*capacity
            return profit
    return profit
price=[24,21,12,10]
items_wt=[7,3,4,5]
capacity=20
print(fractional_knapsack(items_wt,price,capacity))