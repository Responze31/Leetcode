class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l, r = 0, 1
        prices.sort()

        while r <= len(prices):
            if prices[l] + prices[r] > money:
                return money
            elif prices[l] + prices[r] <= money:
                return abs(prices[l] + prices[r] - money)

