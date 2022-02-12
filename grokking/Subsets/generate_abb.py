def generate_generalized_abbreviation(word):
    result = []
    generate_generalized_abbreviation_rec(word,list(),0,0,result)
    return result

def generate_generalized_abbreviation_rec(word,ab_word,start,count,result):
    if start == len(word):
        if count != 0:
            ab_word.append(str(count))
        result.append("".join(ab_word))
    else:
        generate_generalized_abbreviation_rec(word,list(ab_word),start+1,count+1,result)
        if count != 0:
            ab_word.append(str(count))
        new_word = list(ab_word)
        new_word.append(word[start])
        generate_generalized_abbreviation_rec(word,new_word,start+1,0,result)

def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()
