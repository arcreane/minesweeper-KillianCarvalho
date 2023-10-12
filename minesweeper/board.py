import random
import display


def has_win(board):
    for row in board:
        for cell in row:
            state, value = cell[0], cell[1]
            if state == 'C' and value != '💣':
                return False
    return True


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
            if board[new_row][new_col][1] == '💣':
                mine_count += 1

    return mine_count


def reveal_empty_areas(board, coord_x, coord_y):
    if (
            0 <= coord_x < len(board) and
            0 <= coord_y < len(board[0]) and
            board[coord_x][coord_y][0] == 'C'
    ):
        if board[coord_x][coord_y][1] == 0:
            # reveal box if it's empty
            board[coord_x][coord_y][0] = 'R'

            # check adjacent box
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 or dy == 0:
                        reveal_empty_areas(board, coord_x + dx, coord_y + dy)
        else:
            # Si la case n'est pas vide et a une valeur > 0, révélez uniquement cette case
            board[coord_x][coord_y][0] = 'R'


def action_box(board, coord_x, coord_y, action):

    if action == 'R':
        if board[coord_x][coord_y][0] == 'C':
            # Révéler la case si l'action est 'R' et qu'elle est cachée
            if board[coord_x][coord_y][1] == 0:
                # Si la case est vide, révélez les cases adjacentes
                reveal_empty_areas(board, coord_x, coord_y)
            else:
                board[coord_x][coord_y][0] = 'R'
    elif action == 'F':
        board[coord_x][coord_y][0] = 'F'
    elif action == 'U':
        if board[coord_x][coord_y][0] == 'F':
            board[coord_x][coord_y][0] = 'C'
    display.display_board(board)


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
    board = [[['C', 0] for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly on the board
    placed_mines = 0
    while placed_mines < nbr_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        # Check if the cell is already a mine
        if board[row][col][1] == '💣':
            continue

        board[row][col][1] = '💣'
        placed_mines += 1

        # Count mines in neighboring cells
    for row in range(rows):
        for col in range(cols):
            if board[row][col][1] != '💣':
                board[row][col][1] = count_adjacent_mines(board, row, col)

    for line in board:
        for cell in line:
            print(cell[1], end="")
        print()
    return board
