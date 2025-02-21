class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary_str = bin(n)
        # return binary_str.count('1')

        # manual 
        def deciToBin(n):
            if n == 0:
                return '0'
            elif n == 1:
                return '1'
            else:
                return deciToBin(n//2) + str(n%2)

        binary_str = deciToBin(n)
        return binary_str.count('1')