def evaluate_expression(expression):
    return evaluate_expression_rec({},expression)

def evaluate_expression_rec(map,expression):
    if expression in map:
        return map[expression]
    result = []
    if '+' not in expression and '-' not in expression and '*' not in expression:
        result.append(int(expression))
    
    else:
        for i in range(len(expression)):
            char = expression[i]
            if not char.isdigit():
                left_part = evaluate_expression_rec(map,expression[0:i])
                right_part = evaluate_expression_rec(map,expression[i+1:])
                for part1 in left_part:
                    for part2 in right_part:
                        if char == '+':
                            result.append(part1 + part2)
                        if char == '-':
                            result.append(part1 - part2)
                        if char == "*":
                            result.append(part1*part2)
    map[expression] = result
    return result

def main():
  print("Expression evaluations: " +
        str(evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(evaluate_expression("2*3-4-5")))


main()
