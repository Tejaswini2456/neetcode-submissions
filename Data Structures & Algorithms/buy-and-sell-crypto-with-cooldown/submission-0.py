class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = float("-inf")
        rest = 0
        for price in prices[1:]:
            old_hold = hold
            old_sold = sold
            old_rest = rest

            hold = max(old_hold,old_rest-price)
            sold = old_hold + price
            rest = max(old_rest,old_sold)

        return max(sold,rest) 
