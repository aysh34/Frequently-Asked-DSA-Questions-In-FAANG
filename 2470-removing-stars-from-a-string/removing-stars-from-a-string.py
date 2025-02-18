class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if not i == '*':
                st.append(i) 
            elif st and i == '*':
                st.pop()

        return "".join(st)