class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        st=[]
        # [type,colour,size]
        n=len(colors)
        for i in range(n):
            c=colors[i]
            t=types[i]
            if st and st[-1][0]==t and st[-1][1]==c:
                st[-1][2]+=1
            else:
                st.append([t,c,1])
            if st[-1][2]==groupSize[t]:
                st.pop()
        return True if not st else False