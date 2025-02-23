class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -(2**31), 2**31 - 1  # 32-bit integer range
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10  # Extract last digit
            x = x // 10     # Remove last digit

            # Overflow check
            if rev > (MAX // 10) or (rev == MAX // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit  # Build reversed number

        return sign * rev
