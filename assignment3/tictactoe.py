class TictactoeException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Board():
    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    def __init__(self):
        self.board_array = [['' for x in range(3)] for y in range(3)]
        self.turn = 'X'
    def __str__(self):
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("--------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("--------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
        
    
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException ("That's not a valid move")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3
        if self.board_array[row][column] != '':
            raise TictactoeException ('This spot is taken')
        self.board_array[row][column] = self.turn
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X' 

    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == '':
                    cat = False
                else: 
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's game")
        win = False
        for i in range(3):
            if self.board_array[i][0] != '':
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]: #check rows
                    win = True
                    break
        if not win:
            for i in range(3):
                if self.board_array[0][i] != '':
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]: #check columns
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != '':
                if self.board_array[1][1] == self.board_array[0][0] and self.board_array[1][1] == self.board_array[2][2]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == 'X':
                return (False, "X's turn")
            else:
                return (False, "O's turn")
        else:
            if self.turn == 'O':
                return (True, "X wins!")
            else:
                return (True, "O wins!")


board1 = Board()
while True:
    print(board1)
    move = input("Make your move")
    try:
        board1.move(move)
    except TictactoeException as e:
        print(e)
        continue
    result = board1.whats_next()
    if result[0]:
        print (result[1])
        break

