class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        minbuy = prices[0]

        for num in prices:
            maxprof = max(maxprof, num - minbuy)
            minbuy = min(minbuy, num)
        return maxprof      

