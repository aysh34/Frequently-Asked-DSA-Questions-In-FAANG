class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32-bit integer mask

        while b != 0:
            carry = (a & b) & MASK  # Carry in case of 1 1
            a = (a ^ b) & MASK  # sum without carry
            b = (carry << 1) & MASK  # left shift carry

        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)


# a ^ MASK flips all bits of a : This converts the incorrect large positive number into a correct negative representation.

# ~(...) negates it, converting it back to signed form.
