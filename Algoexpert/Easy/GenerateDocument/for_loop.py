def generateDocument(chars,doc):
    for ch in doc:
        documentFrequency = countChar(ch,doc)
        characterFrequency = countChar(ch,chars)
        if documentFrequency > characterFrequency:
            return False
    return True

def countChar(ch,target):
    frequency = 0
    for c in target:
        if c == ch:
            frequency += 1
    return frequency