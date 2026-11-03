def max_min_diff(arr):
    arr.sort()
    n=len(arr)
    mid=n//2
    min,max=0,0
    j=n-1
    for i in range(mid):
        max+=abs(arr[i]-arr[j])
        j-=1
        min+=abs(arr[2*i]-arr[2*i+1])
    print(min,max)
arr=[12,5,25,10,2,15,8,30]
max_min_diff(arr)