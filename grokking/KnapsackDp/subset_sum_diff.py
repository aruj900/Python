def can_partition(num):
    s = sum(num)
    dp = [[-1 for _ in range(s+1)] for _ in range(len(num))]
    return can_partition_rec(dp,num,0,0,0)

def can_partition_rec(dp,num,curr_idx,sum1,sum2):
    if curr_idx == len(num):
        return abs(sum1-sum2)
    if dp[curr_idx][sum1] == -1:
        diff1 = can_partition_rec(dp,num,curr_idx+1,sum1 + num[curr_idx],sum2)
        diff2 = can_partition_rec(dp,num,curr_idx+1,sum1,sum2+num[curr_idx])
        dp[curr_idx][sum1] = min(diff1,diff2)
    return dp[curr_idx][sum1]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()