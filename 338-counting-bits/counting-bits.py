class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [None] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                res[i] = 0
            elif i % 2 == 0:  # even
                res[i] = res[i // 2] # if i is 10 then it has same 1 bits as that of i//2 (i.e 5) has
                
            else:  # odd
                res[i] = res[i // 2] + 1
        return res

        # ans = []
        # for i in range(n+1):
        #     b = bin(i)
        #     ans.append(b.count('1'))

        # return ans
