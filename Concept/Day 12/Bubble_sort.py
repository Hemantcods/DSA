def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr                
a=[1,23,67,843,7,832,65]
print(bubbleSort(a))

# time complexit O(n^2)