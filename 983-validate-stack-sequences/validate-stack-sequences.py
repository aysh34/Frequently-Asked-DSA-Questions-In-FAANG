class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        j = 0 
        
        for num in pushed:
            st.append(num)  
            
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1 
        
        return not st 