def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_sum(slow)
        fast = find_sum(find_sum(fast))
        if slow == fast:
            break
    return slow == 1

def find_sum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit*digit
        num //= 10
    return sum
def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()