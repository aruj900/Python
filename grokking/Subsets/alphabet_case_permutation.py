from sklearn.inspection import permutation_importance


def find_letter_case_string_permutations(str1):
    permutation = []
    permutation.append(str1)
    for i in range(len(str1)):
        if str1[i].isalpha():
            n = len(permutation)
            for j in range(n):
                chs = list(permutation[j])
                chs[i] = chs[i].swapcase()
                permutation.append(''.join(chs))
    return permutation


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()