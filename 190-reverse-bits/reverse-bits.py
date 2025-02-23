class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n,'032b')
        reverse = binary[::-1]
        integer = int(reverse,2)
        return integer