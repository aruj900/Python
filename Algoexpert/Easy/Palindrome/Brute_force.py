#O(n^2) T | O(n) space
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString        

print(isPalindrome("abdba"))