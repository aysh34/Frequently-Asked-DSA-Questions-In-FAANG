class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  
        
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            
            # If we solve this question, we skip the next brainpower questions
            next_valid_question = i + brainpower + 1
            dp[i] = max(dp[i + 1], points + (dp[next_valid_question] if next_valid_question < n else 0))
        
        return dp[0]