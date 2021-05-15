d = {       '0': '0',
	        '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    if not phoneNumber:
	    return []
	
    ans = recursive(0,'',[],phoneNumber)
    return ans

def recursive(i,combo,res,phoneNumber):
	if i == len(phoneNumber):
		res.append(combo)
	else:
		nextDigit = phoneNumber[i]
		children = d[nextDigit]
		for child in children:
			recursive(i+1,combo+child,res,phoneNumber)
		return res
