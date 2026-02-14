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
