from collections import deque
class ParenthesesString:
    def __init__(self,str1,open,closed):
        self.str1 = str1
        self.open = open
        self.closed = closed

def generate_parenthesis(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("",0,0))
    while queue:
        ps = queue.popleft()
        if ps.open == num and ps.closed == num:
            result.append(ps.str1)
        else:
            if ps.open < num:
                queue.append(ParenthesesString(ps.str1 + "(",ps.open + 1,ps.closed))
            if ps.open > ps.closed:
                queue.append(ParenthesesString(ps.str1 + ")",ps.open,ps.closed+1))
    return result

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_parenthesis(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_parenthesis(3)))


main()
