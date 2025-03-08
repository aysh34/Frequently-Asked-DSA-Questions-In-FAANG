class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        res = []
        for i in range(n - k + 1):
            res.append(blocks[i : i + k])
        
        m = float('inf')
        for i in res:
            c = 0
            for j in i:
                if j == 'W':
                    j = 'B'
                    c += 1
            m = min(m,c)

        return m 

        # Count 'W' in the first window of size k
        # min_recolors = blocks[:k].count('W')
        # current_recolors = min_recolors

        # # Slide the window across the string
        # for i in range(k, len(blocks)):
        #     # Remove the outgoing character (left side)
        #     if blocks[i - k] == 'W':
        #         current_recolors -= 1
        #     # Add the incoming character (right side)
        #     if blocks[i] == 'W':
        #         current_recolors += 1

        #     # Update minimum recolors required
        #     min_recolors = min(min_recolors, current_recolors)

        # return min_recolors
