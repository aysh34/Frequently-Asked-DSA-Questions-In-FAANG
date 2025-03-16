class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1  # Minimum possible time
        r = max(ranks) * (cars ** 2)  # in worst case slowest mechanic repairs all cars
        
        def isFeasibleTime(time):
            car_fixed_by_all_mechanics = 0
            for rank in ranks:
                car_fixed_by_all_mechanics += int((time / rank) ** 0.5)
            return car_fixed_by_all_mechanics >= cars

        res = -1
        while l <= r:
            mid = l + (r - l) // 2  # mid is time
            if isFeasibleTime(mid):
                res = mid
                r = mid - 1  # Try to search for even lesser time
            else:
                l = mid + 1
        
        return res