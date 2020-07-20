grid= [["7",".",".",".","4",".",".",".","."], 
 [".",".",".","8","6","5",".",".","."], 
 [".","1",".","2",".",".",".",".","."], 
 [".",".",".",".",".","9",".",".","."], 
 [".",".",".",".","5",".","5",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".",".",".","2",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."]]

def sudoku2(board):
    
# are already seen ,then we know that it is duplicate
        
        seen = set()
        #print(len(board))
        for i in range(len(board)):
            for j in range(len(board[0])):
                curval = board[i][j]
                if curval != '.':
                    row = curval + "found in row" + str(i)
                    col = curval + "found in col" + str(j)
                    smallerboard = curval + "found in board" + str(i//3) + '- ' +  str(j//3)
                    #print(row, col, smallerboard)
                    if (row not in seen) and (col not in seen) and (smallerboard not in seen):
                        seen.add(row)
                        seen.add(col)
                        seen.add(smallerboard)
                    else:
                        return False
        return True

print(sudoku2(grid))