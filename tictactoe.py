import random

def print_board(b):
    for r in b:
        print(" | ".join(r))
        print("-" * 9)

def winner(b , p):
    return any(
        all(b[i][j] == p for j in range(3)) or
        all(b[j][i] == p  for j in range(3))
        for i in range(3)
    ) or all(b[i][i] == p for i in range(3)) or all(b[i][2-i] == p for i in range(3))
def free_cells(b):
    return [(i,j) for i in range(3) for  j in range(3) if b[i][j] == " "]


def computer_move(b):
    for p in ["O","X"]:
        for i,j in free_cells(b):
            b [i][j] = p
            if winner(b , p):
                b [i][j] = " "
                return i,j
            b[i][j] = " "
            return random.choice(free_cells(b))
        
def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    turn = "x"

    while True:
        print_board(board)

        if turn == "x":
            r = input("Enter row number (1,3) or 'q' to quit: ")
            if r.lower() == "q":
                break
            c = input("Enter coloum number (1,3): ")

            try:
                r,c = int(r)-1, int(c)-1
                if not (0 <= r < 3 and 0 <= c < 3):
                    print("INVAILD INPUT pleasse enter a number withen 1 or 3.")
                    continue
                if board[r][c] != " ":
                    print("This position is alredy taken.please chosse postion.")