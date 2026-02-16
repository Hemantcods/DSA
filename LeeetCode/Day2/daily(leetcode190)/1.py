class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit='{:032b}'.format(n & 0xFFFFFFFF)
        
        return int(bit[::-1],2)