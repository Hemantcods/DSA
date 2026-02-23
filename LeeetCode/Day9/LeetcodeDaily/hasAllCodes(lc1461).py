class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashmap=set()
        for i in range(len(s)-k+1):
            sub=s[i:i+k]
            hashmap.add(sub)
            if len(hashmap)==2**k:
                return True
        return False    