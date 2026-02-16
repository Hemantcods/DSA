class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res=""
        carry=0
        # making their length equal
        diff=len(a)-len(b)
        if(diff>0):
            b=("0"*diff)+b
        else:
            a=("0"*(-diff))+a   
        for i in range(len(a)-1,-1,-1):
            total = int(a[i]) + int(b[i]) + carry
            res = str(total % 2) + res  
            carry = total // 2
        if carry:
            res=str(carry)+res
        return res            


