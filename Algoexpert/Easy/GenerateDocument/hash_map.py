def generateDocument(chars,doc):
    characterCounts = {}

    for ch in chars:
        if ch not in characterCounts:
            characterCounts[ch] = 0
        
        characterCounts[ch] += 1
    for ch in doc:
        if ch not in characterCounts or characterCounts[ch] == 0:
            return False
        characterCounts[ch] -= 1
    return True