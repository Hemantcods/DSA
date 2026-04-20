def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i,n):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]  
    return arr      
a=[1,23,67,843,7,832,65]
print(SelectionSort(a))

# time complexit O(n^2)