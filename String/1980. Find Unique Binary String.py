class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=set()
        for i in nums:
            num=int(i,2)
            s.add(num)
        n=len(nums)
        for i in range(int("1"*n)+1):
            print(i)
            if i not in s:
                number=i
                break
        binary=bin(number)[2:]
        return((n-len(binary))*"0"+binary)                            
