class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def diff(word1,word2):
            res=0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    res+=1
                if res>2:
                    return False
            return True
        if len(dictionary) > 0 and len(queries[0]) <= 2:
            return queries
        res=[]
        for word1 in queries:
            for word2 in dictionary:
                if diff(word1,word2):
                    res.append(word1)
                    break
        return res
                         