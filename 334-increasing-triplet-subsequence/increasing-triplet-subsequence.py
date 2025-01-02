class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n1 = float('inf')
        n2 = float('inf')

       for n3 in nums:
            # ju mjhe ab no mila hai agr ye n1 se chota ya equal hai tu n1 mei isko daal do
            if n3 <= n1:
                n1 = n3
            elif n3 <= n2: # n3 agr ye n1 se chota nhi hai tu check kro kiya n2 se chota ya equal hai. agr hai tu n2 mei issy daal do
                n2 = n3
            else: # agr na n1 se chota hai or na nhi n2 se chota hai tu mtlb ye condition n1 < n2 < n3 pora ho gya
                return True
            
        return False
