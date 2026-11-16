# Submission 1 
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n=len(nums)
        left=[0]*n
        right=[0]*n
        st=[]
        # the left Boundary
        for i in range(n):
            while st and nums[i]<nums[st[-1]] and (nums[i] & nums[st[-1]])==nums[i]:
                st.pop()
            if not st:
                left[i]=-1
            else:
                left[i]=st[-1]
            # add to stack
            st.append(i)
        # the right Boundary
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[i]<=nums[st[-1]] and (nums[i] & nums[st[-1]])==nums[i]:
                st.pop()
            if not st:
                right[i]=n
            else:
                right[i]=st[-1]
            # add to stack
            st.append(i)
        ans=0
        for i in range(n):
            ans+=(i-left[i])*(right[i]-i)
        return ans

# Submission 2 with a little space optimisation 
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n=len(nums)
        left=[0]*n
        st=[]
        ans=0
        right=0
        # the left Boundary
        for i in range(n):
            while st and nums[i]<nums[st[-1]] and (nums[i] & nums[st[-1]])==nums[i]:
                st.pop()
            if not st:
                left[i]=-1
            else:
                left[i]=st[-1]
            # add to stack
            st.append(i)
        # the right Boundary
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[i]<=nums[st[-1]] and (nums[i] & nums[st[-1]])==nums[i]:
                st.pop()
            if not st:
                right=n
            else:
                right=st[-1]
            # add to stack
            st.append(i)
            ans+=(i-left[i])*(right-i)
        return ans