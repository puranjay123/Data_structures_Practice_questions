import sys

class Solution(object):
    def maxProfit(self, prices):
        
        """
        :type prices: List[int]
        :rtype: int
        """
#         [7,1,5,3,6,4]
        max_profit,min_price = 0,float('inf')
        for i in prices:
            min_price = min(min_price,i)
            profit = i-min_price
            
            max_profit = max(max_profit,profit)
        return max_profit
            
                
            