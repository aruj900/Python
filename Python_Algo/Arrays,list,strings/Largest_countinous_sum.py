def large_cont_sum(arr):
   
   if len(arr) == 0:
       return 0
   
   max_sum = current_sum = arr[0]
   for num in arr:
       current_sum = max(current_sum + num,num)
       max_sum = max(current_sum,max_sum)
    
   return max_sum
 

        
print(large_cont_sum([1,5,7,-9,4,6,3,7,-3,6,8,-5]))