class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n, m = len(num1), len(num2)
        result = [0] * (n + m)
        
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(n):
            for j in range(m):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                result[i + j] += mul
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()
            
        return ''.join(map(str, result[::-1]))