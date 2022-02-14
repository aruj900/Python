from heapq import *

def find_Kth_smallest(lists, k):
    min_heap = []
    
    for i in range(len(lists)):
        heappush(min_heap,(lists[i][0],0,lists[i]))
    
    number_count, number = 0,0
    while min_heap:
        number, idx , list1 = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(list1) > idx + 1:
            heappush(min_heap,(list1[idx+1],idx+1,list1))
    return number

def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
        