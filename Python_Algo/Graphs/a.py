def mutateTheArray(n, a):
    b = []
    
    b.append(a[0] + a[1])
    print(b)
    for i in range(1,n-1):
        b.append(a[i-1] + a[i] + a[i+1])
    b.append(a[n-1] + a[n-2])
    
    return b

a = [1,2,3,4,5]
n = 5
print(mutateTheArray(n,a))