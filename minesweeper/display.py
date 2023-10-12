import sys
import time
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
|                               Welcome in minesweeper terminal !                              |
|                                                                                              |
|                                       by Qwercus @2023                                       |
+==============================================================================================+
""")


def start_menu():
    return "Choose an action :\n\t1- start a new game\n\t2- load game\n\t3- exit"


def print_difficulty():
    return "Choose a difficulty :\n\t1- Beginner\n\t2- Intermediate\n\t3- Expert\n\t4- Custom"

def display_board(board):
    """
    Display the game board in the console with x-axis numbers at the bottom.

    Args:
        board (list of lists): The game board to be displayed.
    """
    for i, line in enumerate(board):
        print(f"{i} ", end="")
        for cell in line:
            if cell[0] == 'C':
                print("■  ", end="")
            elif cell[0] == 'F':
                print("🚩  ", end="")
            else:
                print(cell[1], " ", end="")
        print()
    # Display number on axis x
    print("   ", end="")
    for col in range(len(board[0])):
        print(f"{col:2} ", end="")
    print("")

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
            if cell == '💣':
                print("💣  ", end="")
            elif cell == 0:
                print("■  ", end="")
            else:
                print(cell, " ", end="")
        print("")

    # Display number on axis x
    print("  ", end="")
    for col in range(cols):
        print(f"{col:2} ", end="")
    print("")


def display_loose():
    text = '''
         __   __                            _                            
         \ \ / /   ___    _  _      o O O  | |      ___     ___     ___  
          \ V /   / _ \  | +| |    o       | |__   / _ \   (_-<    / -_) 
          _|_|_   \___/   \_,_|   TS__[O]  |____|  \___/   /__/_   \___| 
        _| """ |_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|
        "`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
    '''

    lines = text.split('\n')
    width = max(len(line) for line in lines)

    # while True:
    for i in range(width):
        for line in lines:
            print(line[i:i + width])
        time.sleep(0.1)
        sys.stdout.write("\033[F" * len(lines))  # Remonte le curseur pour effacer

def display_win():
    text = '''
          \ \ / /   ___    _  _      o O O\ \    / / (_)    _ _   
          \ V /   / _ \  | +| |    o      \ \/\/ /  | |   | ' \  
          _|_|_   \___/   \_,_|   TS__[O]  \_/\_/  _|_|_  |_||_| 
        _| """ |_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|
        "`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'
    '''

    lines = text.split('\n')
    width = max(len(line) for line in lines)

    # while True:
    for i in range(width):
        for line in lines:
            print(line[i:i + width])
        time.sleep(0.1)
        sys.stdout.write("\033[F" * len(lines))  # Remonte le curseur pour effacer

