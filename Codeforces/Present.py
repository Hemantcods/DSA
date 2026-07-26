'''
Input
The first line contains one integer n (1 ≤ n ≤ 100) — the quantity of friends Petya invited to the party. The second line contains n space-separated integers: the i-th number is pi — the number of a friend who gave a gift to friend number i. It is guaranteed that each friend received exactly one gift. It is possible that some friends do not share Petya's ideas of giving gifts to somebody else. Those friends gave the gifts to themselves.

Output
Print n space-separated integers: the i-th number should equal the number of the friend who gave a gift to friend number i.
'''
'''
Example Input:
    4
    2 3 4 1

Example Output
    4 1 2 3
'''


# we just need to reverse the mapping 
# from sender(ith friend )-> reciver(arr[i])
# to reviver(ith friend )=> sender(ans[i])
def present(n,arr):
    ans=[0]*n
    for i in range(n):
        ans[arr[i]-1]=i+1
    print(ans)
present(4,[2,3,4,1])