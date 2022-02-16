def can_partition(num,sum):
    n = len(num)
    dp = [[False for _ in range(sum+1)]for _ in range(n)]
    for i in range(0,n):
        dp[i][0] = True
    for s in range(1,sum+1):
        dp[0][s] = True if s == num[0] else False
    
    for i in range(1,n):
        for s in range(1,sum+1):
            if dp[i-1][s]:
                dp[i][s] = dp[i-1][s]
            elif s >= num[i]:
                dp[i][s] = dp[i-1][s-num[i]]
    return dp[n-1][sum]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
