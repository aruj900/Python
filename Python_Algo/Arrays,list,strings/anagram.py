import collections

def _anagram(s1,s2):
    
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    if len(s1) != len(s2):
        return False
    
    n_s1 = collections.Counter(s1)
    n_s2 = collections.Counter(s2)
    
    found = True
    for i in n_s1:
        if n_s1[i] != n_s2[i]:
            found = False
            break
    return done
                
print(_anagram('dog','g  d')) 
    
def anagram(s1,s2):
    
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Edge case
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
            
    for k in count:
        if count[k] != 0:
            return False
    return True
