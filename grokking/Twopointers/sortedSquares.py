def make_squares(arr):
    squares = [0 for _ in arr]
    left = 0
    right = len(arr) - 1
    
    for idx in reversed(range(len(arr))):
        small = arr[left]
        large = arr[right]
        if abs(small) > abs(large):
            squares[idx] = small*small
            left += 1
        else:
            squares[idx] = large*large
            right -= 1
    return squares

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()