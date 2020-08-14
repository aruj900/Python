#O(n) T | O(n) S
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)
print(isPalindrome("abdba"))

