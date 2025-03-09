class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        N = n + k-1 # Virtual extended length for circular indexing
        
        i = 0
        j = 1
        count = 0
        while j < N:
            if colors[j % n] == colors[(j - 1) % n]:
                i = j
                j += 1
                continue
            if j - i + 1 == k:
                count += 1
                i += 1
            j += 1
        return count
 
        # count = 0
        # for i in range(n):
        #     valid = True
        #     for j in range(k-1):
        #         # since it's circular
        #         if colors[(i+j)%n] == colors[(i+j+1)%n]:
        #             valid = False # not alternate
        #             break
        #     if valid:
        #         count += 1
        # return count

