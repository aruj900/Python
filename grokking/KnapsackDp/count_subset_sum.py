def count_subsets(num, sum):
    dp = [[-1 for x in range(sum+1)] for y in range(len(num))]
    return count_subsets_rec(dp,num,sum,0)

def count_subsets_rec(dp,num,sum,curr_idx):
    if sum == 0:
        return 1
    n= len(num)
    if n == 0 or curr_idx >= n:
        return 0
    
    if dp[curr_idx][sum] == -1:
        sum1 = 0
        if num[curr_idx] <= sum:
            sum1 = count_subsets_rec(dp,num,sum-num[curr_idx],curr_idx + 1)
        sum2 = count_subsets_rec(dp,num,sum,curr_idx+1)
        dp[curr_idx][sum] = sum1 + sum2
    return dp[curr_idx][sum]

def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()