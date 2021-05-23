class Board:
    def __init__(self):
        self.cells = [" "," "," "," "," ","X"," "," "," ","0"]
    
    def display(self):
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]}")
        print("-----------")
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]}")
        print("-----------")
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]}")


     

board = Board()
board.display()