# Brute Force
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans=0
        for i in range(len(arr1)):
            flag=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    print(abs(arr1[i]-arr2[j]))
                    flag=False
                    break
            if flag:  
                print(i,j)   
                ans+=1
        return ans 
# Time Complexity O(mn)
# Space Complexity O(1)