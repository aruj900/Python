from heapq import *
def find_k_smallest(matrix,k):
    min_heap = []
    
    for i in range(min(k,len(matrix))):
        heappush(min_heap,(matrix[i][0],0,matrix[i]))
    
    number_count, number = 0,0
    while min_heap:
        number,idx,row = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(row) > idx + 1:
            heappush(min_heap,(row[idx+1],idx+1,row))
    return number

def main():
    print("Kth smallest number is: " +
          str(find_k_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()