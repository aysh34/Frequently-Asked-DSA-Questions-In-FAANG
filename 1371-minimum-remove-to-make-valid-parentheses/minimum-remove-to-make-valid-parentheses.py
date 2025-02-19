class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = [] # opening (
        idx = set() # keep track of invalid closing paren
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                if st:
                    st.pop()
                else:
                    idx.add(i) # invalid
        idx.update(st) # unmatched opening parentheses ( are also marked for removal

        res = []
        for i in range(len(s)):
            if i not in idx:
                res.append(s[i])
        return "".join(res)