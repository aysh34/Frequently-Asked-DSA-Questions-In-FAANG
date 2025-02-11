class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        span = 1
        while len(self.st) != 0 and self.st[-1][0] <= price:
            span += self.st[-1][1]
            self.st.pop()

        self.st.append((price,span)) # push in stack with latest span
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)