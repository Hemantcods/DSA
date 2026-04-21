class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        cur=self.difference(source,target)
        if cur==0:
            return 0
        for swp in allowedSwaps:
            swaped=self.swap(source,swp)
            new=self.difference(swaped,target)
            if new<=cur:
                source=swaped
                cur=new
            if new==0:
                return 0
        return cur                    

    def difference(self,source,target):
        res=0
        for i in range(len(source)):
            if source[i]!=target[i]:
                res+=1
        return res                
    def swap(self,source,swap):
        source[swap[0]],source[swap[1]]=source[swap[1]],source[swap[0]]  
        return source  