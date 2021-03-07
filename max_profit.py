class Solution:
    def maxProfit(self, prices):
        start_window = 0
        max_profit = 0
        for end_window in range(len(prices)):
            profit = prices[end_window] - prices[start_window]
            while prices[end_window] < prices[start_window]:
                start_window += 1
            if profit > max_profit:
                max_profit = profit
        return max_profit