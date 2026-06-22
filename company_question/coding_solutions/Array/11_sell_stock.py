'''Best Time to Buy and Sell Stock
Problem Statement
You are given an array prices[] where prices[i] represents the price of a stock on the iᵗʰ day.
You are allowed to buy one stock and sell one stock only once.
Find the maximum profit you can achieve. If no profit is possible, return 0.

Example 1
Input:
prices = [7,1,5,3,6,4]

Output:
5

Explanation:
Buy at price = 1 (Day 2)
Sell at price = 6 (Day 5)
Profit = 6 − 1 = 5

Example 2
Input:
prices = [7,6,4,3,1]

Output:
0

Explanation:
Prices keep decreasing, so no profit can be made.

Approach
At each day:
Keep track of the minimum price seen so far.
Calculate profit if we sell today:
profit = current_price - minimum_price
Update maximum profit.

Dry Run
Input
prices = [7,1,5,3,6,4]
Day	Price	Min Price	Profit	Max Profit
1	7	7	0	0
2	1	1	0	0
3	5	1	4	4
4	3	1	2	4
5	6	1	5	5
6	4	1	3	5

Answer = 5
'''


def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

# Output
# 5


# with best time complexity
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Complexity Analysis
# Complexity	Value
# Time Complexity	O(n)
# Space Complexity	O(1)