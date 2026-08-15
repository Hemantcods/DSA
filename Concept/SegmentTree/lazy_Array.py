# code for SegmentTree range update querry
# we have to find the range sum after the updation querry on array

n = 1

tree = [0] * (4 * n)
lazy = [0] * (4 * n)


def updateRange(start, end, idx, l, r, val):
    # handle the lazy
    if lazy[idx] != 0:
        tree[idx] += (r - l + 1) * lazy[idx]
        # distribut to child
        if r != l:
            lazy[2 * idx + 1] += lazy[idx]
            lazy[2 * idx + 2] += lazy[idx]
        lazy[idx]=0
    # out of bound or invalid case
    if r < start or l > end or l > r:
        return
    # completly inside the range
    if start <= l and end >= r:
        tree[idx] += (r - l + 1) * val
        if l != r:
            # update the lazy nodes of child
            lazy[2 * idx + 1] += val
            lazy[2 * idx + 2] += val
        return
    # overlapping Case
    mid = l + (r - l) // 2
    updateRange(start, end, 2 * idx + 1, l, mid, val)
    updateRange(start, end, 2 * idx + 2, mid + 1, r, val)
    tree[idx]=tree[2*idx+1]+tree[2*idx+2]