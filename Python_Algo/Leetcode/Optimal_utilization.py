a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

def backtrack(a,b,l,r,res):
    if l >=0 and r >=0:
        i, data_i = a[l]
        j, data_j = b[r]
        if data_i + data_j == target and not res:
            res[(i,j)] = True
        elif data_i + data_j < target and not res:
            res[(i,j)] = True
            return res
        backtrack(a,b,l-1,r,res)
        backtrack(a,b,l,r-1,res)


def find_optimal(a,b):
    
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    
    l,r = len(a) -1, len(b) -1
    
    res = {}
    backtrack(a,b,l,r,res)
    return res.keys()
    

print(find_optimal(a,b))