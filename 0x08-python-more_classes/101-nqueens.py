#!/usr/bin/python3
""" Queen's chess"""


from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column_gen(board=[]):
    """Adds a column of zero"""
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """Sets "queen," or 1, to coordinates"""
    board[row][col] = 1


def new_queen_safe(board, row, col):
    """For the board given, checks that for a new queen"""
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # check left
            if board[x][y - i]:
                return False
            # check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(candidates):
    """Converts a board (matrix of 1 and 0)"""
    chess = []
    for x, attempt in enumerate(candidates):
        chess.append([])
        for i, row in enumerate(attempt):
            chess[x].append([])
            for j, col in enumerate(row):
                if col:
                    chess[x][i].append(i)
                    chess[x][i].append(j)
    return chess

candidates = []
candidates.append(board_column_gen())

for col in range(N):
    new_candidates = []
    for matrix in candidates:
        for row in range(N):
            if new_queen_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                add_queen(temp, row, col)
                if col < N - 1:
                    board_column_gen(temp)
                new_candidates.append(temp)
for item in coordinate_format(candidates):
    print(item)
