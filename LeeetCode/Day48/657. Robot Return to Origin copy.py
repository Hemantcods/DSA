class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        for dir in moves:
            if dir=='U':
                x+=1
            if dir=='D':
                x-=1
            if dir=='R':
                y+=1
            if dir=='L':
                y-=1    
        return x==0 and y==0    