class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # withot rotating or without taking extra space
        r,c=len(mat),len(mat[0])
        k=k%c
        if k==0:
            return True
        for i in range(r):
            for j in range(c):
                if i%2==0:
                    if mat[i][j]!=mat[i][(j+k)%c]:
                        return False
                else:
                    if mat[i][j]!=mat[i][(j-k+c)%c]:
                        return False
        return True                    
