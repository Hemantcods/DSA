class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        s=set()
        for obs in obstacles:
            key=str(obs[0])+'_'+str(obs[1])
            s.add(key)

        x,y=0,0
        maxDis=0
        dir=[0,1]
        for i in range(len(commands)):
            if commands[i]==-2:
                dir[0],dir[1]=-dir[1],dir[0]
            elif commands[i]==-1:
                dir[0],dir[1]=dir[1],-dir[0]
            else:
                for j in range(commands[i]):
                    newX=x+dir[0]
                    newY=y+dir[1]
                    newStr=str(newX)+'_'+str(newY) 
                    if newStr in s:
                           break
                    else:
                        x=newX
                        y=newY 
            maxDis=max(maxDis,x**2 + y**2)   
        return maxDis             