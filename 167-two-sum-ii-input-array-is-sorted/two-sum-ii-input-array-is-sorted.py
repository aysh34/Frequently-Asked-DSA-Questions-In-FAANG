class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array is sorted we can use two-pointer approach
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
