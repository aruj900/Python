import collections
def partition_label(S):
    
    rc = set()
    r = []
    d = collections.Counter(S)
    
    partition = ""
    
    for i,c in enumerate(S):
        partition += c
        if d[c] != 1:
            rc.add(c)
            d[c] = d[c] - 1
        else:
            if (c in rc): rc.remove(c)
        
        if len(rc) == 0:
            r.append(partition)
            partition = ""
    print(r)        
    return [len(w) for w in r]
print(partition_label("ababcbacadefegdehijhklij"))
   