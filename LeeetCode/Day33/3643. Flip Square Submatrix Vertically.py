class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        upper=x
        lower=x+k-1

        while upper<=lower:
            u_row=grid[upper]
            l_row=grid[lower]
            for index in range(y,y+k):
                u_row[index],l_row[index]=l_row[index],u_row[index]

            upper+=1
            lower-=1
        return grid        