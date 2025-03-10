# Python program to implement Stock Buy 
# and Sell – Max 2 Transactions Allowed

def maxProfit(price):
    n = len(price)
    
    # Create profit array and initialize it as 0
    profit = [0] * n

    # Get the maximum profit with only one transaction 
    # allowed. After this loop, profit[i] contains
    # maximum profit from price[i..n-1] using at most
    # one transaction.
    maxPrice = price[-1]
    for i in range(n - 2, -1, -1):
      
        # maxPrice has maximum of price[i..n-1]
        maxPrice = max(maxPrice, price[i])

        # Update profit[i]
        profit[i] = max(profit[i + 1], maxPrice - price[i])

    # Variable to store the maximum 
    # profit using two transactions
    res = 0
    minPrice = price[0]
    for i in range(1, n):
      
        # minPrice is the minimum price in price[0..i]
        minPrice = min(minPrice, price[i])

        # Calculate the maximum profit by adding 
        # the profit of the first transaction
        res = max(res, profit[i] + (price[i] - minPrice))

    return res

if __name__ == "__main__":
    price = [10, 22, 5, 75, 65, 80]
    print(maxProfit(price))
