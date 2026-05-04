def find_min_max(arr,st,ed):
    if st==ed:
        return arr[st],arr[ed]
    if(st+1==ed):
        if (arr[st]<arr[ed]):
            return arr[st],arr[ed]
        else:
            return arr[ed],arr[st] 
    mid=(st+ed)//2
    min1,max1=find_min_max(arr,st,mid)
    min2,max2=find_min_max(arr,mid+1,ed)
    return min(min1,min2),max(max1,max2)
arr=[1,25,7,3,6,8,2]
print(find_min_max(arr,0,len(arr)-1))