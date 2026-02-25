class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        flag=True
        length=len(arr)
        while(flag):
            flag=False
            for i in range(length-1):
                if bin(arr[i]).count("1")>bin(arr[i+1]).count("1"):
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    flag=True
                if bin(arr[i]).count("1")==bin(arr[i+1]).count("1"):
                    if arr[i]>arr[i+1]:
                        arr[i],arr[i+1]=arr[i+1],arr[i]
                        flag=True
        return arr            

