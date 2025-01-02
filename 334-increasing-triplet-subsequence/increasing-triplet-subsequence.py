class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n1 = float('inf')
        n2 = float('inf')

        for n3 in nums:
            if n3 <= n1:
                n1 = n3
            elif n3 <= n2:
                n2 = n3
            else:
                return True
            
        return False