import collections
def minWindow(s,t):
    need,missing = collections.Counter(t), len(t)
    i,j,mwStart,mwEnd = 0,1,0,0
    while j < len(s):
        if need[s[j]] > 0:
            missing -= 1
        need[s[j]] -= 1
        if missing == 0:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not mwEnd or j - i <= mwEnd - mwStart:
                mwStart,mwEnd = i,j
            j += 1
    return s[mwStart:mwEnd]



