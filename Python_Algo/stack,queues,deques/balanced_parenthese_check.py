def balance_check(s):
    
    if len(s)%2 != 0:
        return False
    opening = set('([{')
    closing = set(')]}')
    
    matches = set([('(',')'), ('[',']'),('{','}')])
    
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        
        elif paren in closing:
            
            if len(stack) == 0:
                return False
            
            last_open = stack.pop()
            
            if (last_open,paren) not in matches:
                return False
        else:
            continue
    return len(stack) == 0
    
print(balance_check('(a)'))

