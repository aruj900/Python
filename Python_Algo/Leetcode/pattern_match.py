def pattern(p,s):
    new_s = replace_vowels(s)
    final_s = replace_coff(new_s)
    l_p = len(p)
    l_s = len(s)
    sub = []
    for i in range(0,(l_s-l_p)):
        temp = final_s[i:i+l_p]
        sub.append(temp)
    cnt = 0
    for i in sub:
        if i == p:
            cnt +=1
    return cnt
        
        
    

def replace_vowels(t):
    vowels = ['a','e','i','o','u']
    for c in t:
        if c in vowels:
            t = t.replace(c,'0')
    return t

def replace_coff(f):
    vowels = ['a','e','i','o','u','0']
    for c in f:
        if c not in vowels:
            f = f.replace(c,'1')
    return f
    


print(pattern('010','amazing'))
            
        