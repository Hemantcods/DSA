class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        flag=s[0]
        count=0
        prev=0
        curr=0
        for i in s:
            if i==flag:
                curr+=1
            else:
                count+=min(prev,curr)
                prev=curr
                curr=1
                flag=i
        return count+min(prev,curr)                
