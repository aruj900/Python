def index_prod(lst):
    
    output = [None] * len(lst)
    
    product = 1
    i = 0
    
    while i < len(lst):
        output[i] = product
        
        product *= lst[i]
        
        i += 1
        
    
    product = 1
    i = len(lst) - 1
    
    while i >= 0:
        
        output[i] *= product
        product *= lst[i]
        i -= 1
    return output

print(index_prod([1,2,3,4,5]))