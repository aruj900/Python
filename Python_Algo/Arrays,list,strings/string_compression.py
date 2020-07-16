import collections
def compress(s):
    out = ''
    s1 = collections.Counter(s)
    for i,key in s1.items():
        out = out + i+str(key)    
    return out
    
    
print(compress("AAAAAAAAAAAAAddddddddddsssssss"))

def compress1(s):
    
    r = ""
    l = len(s)
    
    if l == 0:
        return 0
    if l == 1:
        return s+"1"
    
    cnt =1
    i = 1
    
    while i < l:
        if s[i] == s[i - 1]:
            
            cnt +=1
        
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1
        i +=1
    r = r + s[i - 1] + str(cnt)
    
    return r
print(compress1("AAAAAAAAAAAAAddddddddddsssssss"))