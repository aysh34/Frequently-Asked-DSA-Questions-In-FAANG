class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        m = len(popped)

        st = []
        i = j = 0
        while i < n and j < m:
            st.append(pushed[i])

            while len(st) != 0 and j < m and st[-1] == popped[j]:
                st.pop()
                j += 1

            i += 1

        return len(st) == 0