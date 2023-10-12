import sys
import config
import board as board_controller
import input_handler
import display

def get_valid_difficulty(input_handler, display):
    """
        This function prompts the user to choose a difficulty level and returns a valid choice.

        Args:
            input_handler: An object that handles user input.
            display: An object that provides user interface for displaying options.

        Returns:
            int: A valid difficulty choice (1, 2, or 3).

        Note:
        - If the user enters 1, 2, or 3, the function returns that choice.
        - If the user enters 4, it prints a message indicating that this option is not currently available.
        - If the user enters any other value, it prints an error message and prompts for input again.
    """
    difficulty_choice = input_handler.get_int_user(display.print_difficulty())
    if 1 <= difficulty_choice <= 3:
        return difficulty_choice
    elif difficulty_choice == 4:
        print("Sorry, it currently doesn't work. Wait for the next version.")
    else:
        print("It's not a valid option")

    return get_valid_difficulty(input_handler, display)

def start_game():
    """
    Starts the Minesweeper game.

    This function displays the welcome message, allows the user to choose an action to start the game
    (e.g., start a new game, load a saved game, or exit the game), and choose the game difficulty.

    The function handles user input and initializes the game board accordingly.

    Returns:
        None
    """

    # say hello
    display.print_welcome()

    # Choose an action to start game and choose a difficulty
    start = False
    while not start:
        user_action = input_handler.get_int_user(display.start_menu())
        # 1->  start the game # 2-> charge game # 3 -> exit
        if user_action == 1:
            start = True
            difficulty_choice = get_valid_difficulty(input_handler, display)
            board = board_controller.initialize_board(config.CONFIG_DIFFICULTY[difficulty_choice - 1][0], config.CONFIG_DIFFICULTY[difficulty_choice - 1][1])
            play_game(board)
        elif user_action == 2:
            # charge game
            print("Sorry, the load functionality is for another version.")
        elif user_action == 3:
            sys.exit()
        else:
            print("It's not a choice option")

def play_game(board):
    """
        Function to play a game on a given board.

        Args:
        board (list): A list representing the game state.

        Returns:
        None

        The function displays the board and then starts a game loop. Players can take actions by entering commands
        via input_handler.get_user_action(), and the game continues until a player wins or a bomb explodes.

        If a player steps on a bomb, the game ends and displays a failure message. If the player successfully achieves
         the game's objective (possibly defined in board_controller.has_win()), the game ends with a success message.

        Example usage:
        board = initialize_board()
        play_game(board)
    """
    game_over = False
    display.display_board(board)
    while not game_over:
        user_action = input_handler.get_user_action()
        if user_action[2] == 'R':
            if board[user_action[0]][user_action[1]][1] == "💣":
                print("BOOM ! You have failed ! Try again")
                game_over = True
        board_controller.action_box(board, user_action[0], user_action[1], user_action[2])
        if board_controller.has_win(board):
            print("GG Well play !")
            game_over = True

if __name__ == "__main__":
    start_game()
