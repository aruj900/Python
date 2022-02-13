def search_next_letter(letters,key):
    n = len(letters)
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end)//2
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % n]
def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()