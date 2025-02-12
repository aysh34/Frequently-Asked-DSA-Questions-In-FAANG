class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        st = []
        left = [0] * n
        right = [0] * n 
        count = 0 # no of consecutive elements till arr[i] is minimum
        res = 0

        # step 1: populate left
        for i in range(n):
            count = 1
            while st and st[-1][0] > arr[i]:
                count += st[-1][1]
                st.pop() # pop the element with its count

            left[i] = count 
            # ab current element ko with its count push krdo
            st.append((arr[i],count))
        st.clear()

        # step 2: populate right
        for i in range(n-1, -1, -1):
            count = 1
            while st and st[-1][0] >= arr[i]: # >= to handle duplicates
                count += st[-1][1] # ek or aisa element mil gya jisse curr chota hai
                st.pop() # pop the element with its count

            right[i] = count 
            # ab current element ko with its count push krdo
            st.append((arr[i],count))

        # step 3: arr[i] * left [i] * right[i]
        for i in range(n):
            res += arr[i] * left[i] * right[i]

        return res % mod


        # res = 0

        # for start in range(len(arr)):
        #     for end in range(start, len(arr)):
        #         res += min(arr[start:end+1])

        # return res 
        # TC: O(n3)