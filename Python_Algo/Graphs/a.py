def pair_sum(arr,k):
    
    if len(arr) < 2:
        return 
    seen = set()
    output = set()
    
    for i in arr:
        target = k - i
        
        if target not in seen:
            seen.add(i)
            
        else:
            output.add((min(i,target),max(i,target)))
    print('\n'.join(map(str,list(output))))

print(pair_sum([1,3,2,9,5,6],11))