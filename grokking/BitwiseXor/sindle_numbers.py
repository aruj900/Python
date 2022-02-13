def find_single_numbers(nums):
    ans = [-1,-1]
    temp = 0
    for i in nums:
        temp ^= i
    
    for i in nums:
        if (temp^i in nums):
            ans[0] = temp^i
            ans[1] = i
            break
    return ans

def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()