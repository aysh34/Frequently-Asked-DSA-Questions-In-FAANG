class Solution:
    def simplifyPath(self, path: str) -> str:
        splits = path.split('/')
        st = []
        res = ""

        for i in splits:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if st:
                    st.pop()
            else:
                st.append(i)
            
        return '/' + "/".join(st)