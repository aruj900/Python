def remove_duplicates(arr):
    
    next_none_duplicate = 1
    i = 1
    while (i < len(arr)):
        if arr[next_none_duplicate - 1] != arr[i]:
            arr[next_none_duplicate] = arr[i]
            next_none_duplicate += 1
        i + 1
    return next_none_duplicate

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()