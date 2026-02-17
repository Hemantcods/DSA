class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map=defaultdict(list)
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord("a")]+=1
            char_map[tuple(count)].append(i)  
        return list(char_map.values())
