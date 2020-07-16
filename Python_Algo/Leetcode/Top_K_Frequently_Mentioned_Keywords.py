from collections import Counter
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular deltacellular.",
]

def topkey(k,keywords,reviews):
    word_list = []
    output = []
    for i in reviews:
        word_list.extend(i.lower().replace(',','').split(' '))
   # print(word_list)
    count = Counter(word_list)
    print(count)
    temp = list(count.keys())
    #print(temp)
    for key in keywords:
        if key in temp:
            output.append(key)
            
    
           
    output.sort(key = lambda i: (-count[i],i))       
    print(output)

print(topkey(k,keywords,reviews))