import math
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(self,mid,workerTimes,mh):
            h=0
            for i in range(len(workerTimes)):
                h+=int((math.sqrt((2*mid/workerTimes[i])+0.25))-0.5)
                if h>=mh:
                    return True
            return False
        maxTime=max(workerTimes)
        l=1
        r=int(maxTime*mountainHeight*(mountainHeight+1)/2)
        result=0
        while(l<=r):
            mid=int(l+(r-l)/2)
            if(check(self,mid,workerTimes,mountainHeight)):
                result=mid
                r=mid-1
            else:
                l=mid+1
        return result    