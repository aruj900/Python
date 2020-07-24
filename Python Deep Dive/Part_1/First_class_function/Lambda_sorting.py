l = ['c','B','D','a']
print(sorted(l,key=lambda s: s.upper()))

d = {'def':300,'abc':200,'ghi':100}
print(d)

print(sorted(d))

print(sorted(d, key=lambda e: d[e]))


def dist_sq(x):
    return (x.real)**2 + (x.imag)**2
print(dist_sq(1+1j))

l = [3+3j,1-1j,0,3+0j]
print(sorted(l,key=dist_sq))


print(sorted(l,key=lambda x: (x.real)**2 + (x.imag)**2))

l =['cleese','Idle','Palin','Chapman','Gilliam','Jones']

print(sorted(l))

print(sorted(l,key=lambda s:s[-1]))

#the sorted is stable sort i.e if equal then function which is called first will be printed first

