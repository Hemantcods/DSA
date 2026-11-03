class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        robots = list(range(n))
        
        # Sort by position
        robots.sort(key=lambda i: positions[i])
        
        stack = []
        
        for i in robots:
            if directions[i] == 'R':
                stack.append(i)
            else:
                # Moving left → possible collision
                while stack and healths[i] > 0:
                    j = stack[-1]
                    
                    if healths[j] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                        healths[j] = 0
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                    else:
                        stack.pop()
                        healths[i] = 0
                        healths[j] = 0
        
        # Collect survivors
        result = []
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])
        
        return result