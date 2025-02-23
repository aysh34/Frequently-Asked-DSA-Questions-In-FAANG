class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)  
            n >>= 1 
        return result
        # binary = format(n,'032b')
        # reverse = binary[::-1]
        # integer = int(reverse,2)
        # return integer