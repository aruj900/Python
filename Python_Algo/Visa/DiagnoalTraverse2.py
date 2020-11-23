import collections
def findDiagnol(nums):
    dic = collections.defaultdict(list)
    ans = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            dic[i+j].append(nums[i][j])
    for _,v in dic.items():
        for item in reversed(v):
            ans.append(item)
    return ans

print(findDiagnol([[1,2,3],[4,5,6],[7,8,9]]))