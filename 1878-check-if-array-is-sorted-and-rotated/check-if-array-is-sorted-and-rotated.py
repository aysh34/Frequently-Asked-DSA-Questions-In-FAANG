class Solution:
    def check(self, nums: List[int]) -> bool:
        # agr array sorted thi or phir rotate hoi tu exactly 'ek' aisa break point ho ga jaha aisa ho ga arr[i] > arr[i+1]

        break_point = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]: # circular index calculate (i+1) % n
                break_point += 1
       
        return break_point <= 1