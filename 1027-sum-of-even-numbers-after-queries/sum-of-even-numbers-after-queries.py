from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)  # Initial sum of even numbers
        res = []
        
        for val, index in queries:
            if nums[index] % 2 == 0:  # If the current number is even, remove it from even_sum
                even_sum -= nums[index]
            
            nums[index] += val  # Update the number
            
            if nums[index] % 2 == 0:  # If the updated number is even, add it to even_sum
                even_sum += nums[index]
            
            res.append(even_sum)  # Store the current even_sum
        
        return res
