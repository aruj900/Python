import collections
def findDiagnoal(matrix):
    if not matrix or not matrix[0]:
        return []
    d = collections.defaultdict(list)
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            d[i+j].append(matrix[i][j])
    ans = []
    for k in d:
        if k % 2 == 0:
            [ans.append(x) for x in reversed(d[k])]
        else:
            [ans.append(x) for x in d[k]]
    return ans
print(findDiagnoal([[1,2,3],[4,5,6],[7,8,9]]))