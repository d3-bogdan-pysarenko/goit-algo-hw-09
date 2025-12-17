coins_list_a = [50, 25, 10, 5, 2, 1]
coins_list_b = [10, 6, 1]

def find_coins_greedy(amount, coins):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    current_amount = amount

    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------


# Testing time - Example a
print(f"Results for Greedy function, set A -> {find_coins_greedy(113, coins_list_a)}")
print(f"Results for Dynamic function, set A -> {find_min_coins(113, coins_list_a)}")

# Testing time - Example b
print(f"Results for Greedy function, set B -> {find_coins_greedy(12, coins_list_b)}")
print(f"Results for Dynamic function, set B -> {find_min_coins(12, coins_list_b)}")

