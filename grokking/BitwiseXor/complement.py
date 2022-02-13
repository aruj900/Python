import math
def calculate_bitwise_complement(n):
  bit_count = math.floor(math.log2(n)) + 1
  all_bits_set = pow(2, bit_count) - 1

  return n^all_bits_set

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()