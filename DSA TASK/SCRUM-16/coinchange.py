def min_coins(coins, amount):
    # Initialize an array to store the minimum number of coins for each amount from 0 to amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins are needed to make amount 0

    # Iterate through each amount from 1 to amount
    for i in range(1, amount + 1):
        # Check each coin denomination
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still float('inf'), it means it's not possible to make up the amount with the given coins
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
amount = 11
result = min_coins(coins, amount)
print(result)  # Output: 3 (11 = 5 + 5 + 1)
