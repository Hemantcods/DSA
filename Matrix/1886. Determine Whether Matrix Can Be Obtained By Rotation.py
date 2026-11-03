class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True
        n=1
        while(n<4):
            for i in range(len(mat)):
                for j in range(i, len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
            # Reverse each row
            for row in mat:
                row.reverse()
            n+=1
            if mat==target:
                return True
        return False        