def caesarCipher(string,key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey,alphabet))
    return "".join(newLetters)

def getNewLetter(letter,key,alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode%25]

print(caesarCipher("fhg",4))