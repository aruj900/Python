products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"

def binary_search(arr,word):
    
            
    first = 0
    last = len(arr) 
            
            
            
    while first < last:
        mid = (first + last)//2
                
              
                    
        if arr[mid] < word:
            first = mid + 1
                
        else:
            last = mid
                   
    return first
        
        
def suggestedProducts(products,searchWord):
        
    products.sort()
    s = ''
    ans = []
        
       
        
    for ch in searchWord:
            
        s = s + ch
        l = len(s)
        temp_arr = []
            
        index = binary_search(products,s)
            
        for i in range(index,min(len(products),index+3)):
            if products[i][0:l] == s:
                temp_arr.append(products[i])
        ans.append(temp_arr)
    return ans

print(suggestedProducts(products,searchWord))    


       

        

