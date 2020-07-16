def finder(arr1,arr2):
    
   arr1.sort()
   arr2.sort()
   
   for num1,num2 in zip(arr1,arr2):
       if num1 != num2:
           return num1
   
   return arr1[-1]

arr1 = [2,4,7,3,9]
arr2 = [2,4,9,7]

print(finder(arr1,arr2))