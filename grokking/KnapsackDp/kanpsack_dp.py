def solve_knapsack(profits,weights,capacity):
    dp = [[-1 for i in range(capacity+1)] for j in range(len(profits))]
    return knapsack_rec(dp,profits,weights,capacity,0)

def knapsack_rec(dp,profits,weights,capacity,curr_idx):
    if capacity <= 0 or curr_idx >= len(profits):
        return 0
    if dp[curr_idx][capacity] != -1:
        return dp[curr_idx][capacity]
    profit1 = 0
    if weights[curr_idx] <= capacity:
        profit1 = profits[curr_idx] + knapsack_rec(dp,profits,weights,capacity-weights[curr_idx],curr_idx+1)
    profit2 = knapsack_rec(dp,profits,weights,capacity,curr_idx+1)
    
    dp[curr_idx][capacity] = max(profit1,profit2)
    return dp[curr_idx][capacity]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()