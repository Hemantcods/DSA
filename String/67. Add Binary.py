# Approach 1: Pad the shorter string, then add digit by digit
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


# Approach 2: Two pointers from the end
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1 
            if j >= 0:
                total += int(b[j])
                j -= 1
            res = str(total % 2) + res
            carry = total // 2
        return res            
