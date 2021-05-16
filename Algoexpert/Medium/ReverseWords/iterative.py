def reverseWordsInString(string):
    # Write your code here.
    words = []
    startOfWord = 0
    for idx in range(len(string)):
	    character = string[idx]
		
	    if character == " ":
		    words.append(string[startOfWord:idx])
		    startOfWord = idx
	    elif string[startOfWord] == " ":
		    words.append(" ")
		    startOfWord = idx
    words.append(string[startOfWord:])
    reverseList(words)
	
    return "".join(words)
def reverseList(list):
	start,end = 0,len(list) -1
	while start < end:
		list[start], list[end] = list[end], list[start]
		start += 1
		end -= 1
		
