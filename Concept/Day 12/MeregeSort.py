def Divide(arr,left,right):
    if (left<right):
        m=(left+right)//2
        Divide(arr,1,m)
        Divide(arr,m+1,right)
        Merge(arr,left,m,right)
        return arr

def Merge(arr,left,middle,right):
    s1=middle-left+1
    s2=right-middle
    L=[0]*s1
    R=[0]*s2
    for i in range(s1):
        L[i]=arr[left+i]
    for j in range(s2):
        R[j]=arr[middle+1+j]
    i=j=0
    k=left
    while(i<s1 and j<s2):
        if (L[i]<R[j]):
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while(i<s1):    
        arr[k]=L[i]
        i+=1
        k+=1
    while(j<s2):
        arr[k]=R[j]
        j+=1
        k+=1
a=[1,23,67,843,7,832,65]
print(Divide(a,0,len(a)-1))    



        