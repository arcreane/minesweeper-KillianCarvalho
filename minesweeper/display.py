def print_welcome():
    print("""
+==============================================================================================+
|                                                                                              |
|  ███╗   ███╗██╗███╗   ██╗███████╗███████╗██╗    ██╗███████╗███████╗██████╗ ███████╗██████╗   |
|  ████╗ ████║██║████╗  ██║██╔════╝██╔════╝██║    ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗  |
|  ██╔████╔██║██║██╔██╗ ██║█████╗  ███████╗██║ █╗ ██║█████╗  █████╗  ██████╔╝█████╗  ██████╔╝  |
|  ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ╚════██║██║███╗██║██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗  |
|  ██║ ╚═╝ ██║██║██║ ╚████║███████╗███████║╚███╔███╔╝███████╗███████╗██║     ███████╗██║  ██║  |
|  ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝  |
|                                                                                              |
|                                                                                              |
|                                                                                              |
|                                                                                              |
|                                   Welcome in minesweeper terminal !                          |
|                                                                                              |
|                                           by Qwercus @2023                                   |
+==============================================================================================+
""")


def start_menu():
    return "Choose an action :\t\n1- start a new game\n2- load game\n3- exit"


def print_difficulty():
    return "Choose a diffculty :\t\n1- Beginner\n2- Intermediate\n3- Expert\n4- Custom"


def display_board(board):
   for line in board:
       for cell in line:
           if cell[0] == 'C':
               print("C", end=" ")
           elif cell[0] == 'F':
               print("F", end=" ")
           else:
               print(cell[1], end=" ")
       print()

def display_solution(board):
    """
    Display the game board in the console with x-axis numbers at the bottom.

    Args:
        board (list of lists): The game board to be displayed.
    """
    rows, cols = len(board), len(board[0])

    # Display grid
    for row in range(rows):
        print(f"{row:2} ", end="")
        for col in range(cols):
            cell = board[row][col]
            if cell == 'X':
                print("💣", end=" ")
            elif cell == 0:
                print("■", end=" ")
            else:
                print(cell, end=" ")
        print("")

    # Display number on axis x
    print("  ", end="")
    for col in range(cols):
        print(f"{col:2} ", end="")
    print("")