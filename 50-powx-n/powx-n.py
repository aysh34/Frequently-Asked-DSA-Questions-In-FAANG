class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n # O(1)

        if n == 0:
            return 1
        if n < 0: # -ve
            n = -n # make it +ve
            x = 1 / x

        half = self.myPow(x,n//2)
        
        if n % 2==0: # even
            return half * half
        else:
            return half * half * x

# x^n == x ^ (n/2) * x ^ (n/2) if n even
# x^n == x * x ^ (n - 1) if n odd
