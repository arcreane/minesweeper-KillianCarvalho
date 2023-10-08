import random


def count_adjacent_mines(board, row, col):
    """
    Count the number of mines adjacent to the specified cell.

    Args:
        board (list of lists): The game board.
        row (int): The row of the cell to check.
        col (int): The column of the cell to check.

    Returns:
        int: The number of adjacent mines.
    """
    rows, cols = len(board), len(board[0])
    mine_count = 0

    # Define the eight possible directions to check adjacent cells
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the adjacent cell is within the bounds of the board
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if board[new_row][new_col] == 'X':
                mine_count += 1

    return mine_count


def initialize_board(grid_size, nbr_mines):
    """
    Initialize the game board with the given grid size and number of mines.

    Args:
        grid_size (tuple): A tuple containing the number of rows and columns for the game grid.
        nbr_mines (int): The number of mines to place on the grid.

    Returns:
        list of lists: The initialized game board.
    """
    rows, cols = grid_size
    board = [[0] * cols for _ in range(rows)]

    # Place mines randomly on the board
    placed_mines = 0
    while placed_mines < nbr_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        # Check if the cell is already a mine
        if board[row][col] == 'X':
            continue

        board[row][col] = 'X'
        placed_mines += 1

        # Count mines in neighboring cells
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != 'X':
                board[row][col] = count_adjacent_mines(board, row, col)

    print(board)
    return board
