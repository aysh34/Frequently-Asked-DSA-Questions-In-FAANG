from typing import List

class Solution:
   def checkValidCuts(self,n, rectangles):
        def can_cut(rectangles, axis):
            rectangles.sort(key=lambda x: x[axis])
            cuts, previous_end = 0, -1

            for rect in rectangles:
                start, end = rect[axis], rect[axis + 2]

                if start >= previous_end:
                    cuts += 1
                previous_end = max(previous_end, end)
                if cuts >= 3:
                    return True

            return False
        return can_cut(rectangles, 0) or can_cut(rectangles, 1)
