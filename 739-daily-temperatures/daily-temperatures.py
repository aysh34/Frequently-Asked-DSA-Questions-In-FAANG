class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Next larger element
        
        n = len(temperatures)
        st = [] # store index
        res = [0] * n
        for i in range(n-1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()

            if not st: # no larger element in right
                res[i] = 0
            else:
                res[i] = st[-1] - i

            st.append(i)
        return res


                        
        # n = len(temperatures)
        # ans = []
        # for i in range(n):
        #     c = 0
        #     for j in range(i+1,n):
        #         if temperatures[j] > temperatures[i]:
        #             c = j - i #  Store day difference
        #             break
        #     ans.append(c)
        # return ans      