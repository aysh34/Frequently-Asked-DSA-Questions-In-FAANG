class DetectSquares:

    def __init__(self):
        self.map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.map[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        queryX, queryY = point
        total = 0
        for (px,py), freq in list(self.map.items()):
            # find diagonal
            if abs(px-queryX) == abs(py-queryY) and px != queryX and py != queryY:
                # found the diagonal now find other two points
                total += freq * self.map[(px, queryY)] * self.map[(queryX, py)]
        return total


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)