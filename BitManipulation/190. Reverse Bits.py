# Approach 1: Format to 32-bit binary string, reverse, then parse
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit='{:032b}'.format(n & 0xFFFFFFFF)
        
        return int(bit[::-1],2)


# Approach 2: Bit-by-bit shifting
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


# Approach 3: Binary string with zero padding
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((bin(n)[2:].zfill(32))[::-1],2)
