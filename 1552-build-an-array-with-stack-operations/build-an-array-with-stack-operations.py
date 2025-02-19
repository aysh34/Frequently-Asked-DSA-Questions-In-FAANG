class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        i = 0 
        stream = 1 # [1,n]

        while i < len(target) and stream <= n:
            arr.append("Push") # push current stream element

            if stream == target[i]: # correct element is pushed
                i += 1 
            else:
                arr.append("Pop")
            stream += 1

        return arr