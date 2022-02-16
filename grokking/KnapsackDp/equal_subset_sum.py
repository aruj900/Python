def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    
    dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
    return True if can_partition_rec(dp,num,int(s/2),0) == 1 else False

def can_partition_rec(dp,num,sum,curr_idx):
    if sum == 0:
        return 1
    n = len(num)
    if n == 0 or curr_idx >= n:
        return 0
    
    if dp[curr_idx][sum] == -1:
        if num[curr_idx] <= sum:
            if can_partition_rec(dp,num,sum - num[curr_idx],curr_idx+1) == 1:
                dp[curr_idx][sum] = 1
                return 1
        dp[curr_idx][sum] = can_partition_rec(dp,num,sum,curr_idx+1)
    return dp[curr_idx][sum]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
    