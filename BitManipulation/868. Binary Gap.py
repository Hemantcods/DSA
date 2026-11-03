class Solution:
    def binaryGap(self, n: int) -> int:
        arr=[]
        binary=bin(n)[2:]
        for i in range(len(binary)):
            if binary[i]=="1":
                arr.append(i)
        res=0
        print(binary)
        if len(arr)>1:
            for j in range(len(arr)-1):
                res=max(res,arr[j+1]-arr[j])
        else:
            return 0        
        return res

