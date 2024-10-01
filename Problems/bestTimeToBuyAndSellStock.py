"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""

from typing import List


def maxProfit(prices: List[int]) -> int:
        if(len(prices) <= 1):
            return 0

        i = 1        
        max_num = max(prices[i:len(prices)]) 
        
        max_profit = max(0, max_num - prices[0])

        # -1 because we don't care about the last value
        while i < len(prices): 

            if prices[i] == max_num:
                if i != len(prices) - 1:
                    max_num = max(prices[i+1:len(prices)])
                max_profit = max(max_profit, prices[i] - min(prices[0:i]))
            i+=1    

        return max_profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))


# O(n) time complexity using two pointers
def maxProfit2(prices: List[int]) -> int:
    if(len(prices) <= 1):
        return 0

    l = 0
    r = l + 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(max_profit, prices[r] - prices[l])
        else:
            l = r

        r += 1
    
    return max_profit
        

print(maxProfit2([7,1,5,3,6,4]))
print(maxProfit2([7,6,4,3,1]))
         
         


     