import sys
import config
import board as board_controller
import input_handler
import display

def start_game():
    # say hello
    display.print_welcome()

    # Choose an action to start game and choose a difficulty
    start = False
    while not start:
        user_action = input_handler.get_int_user(display.start_menu())
        if user_action == 1:
            start = True
            valid_diff = False
            while not valid_diff:
                difficulty_choice = input_handler.get_int_user(display.print_difficulty())
                if 1 <= difficulty_choice <= 3:
                    valid_diff = True
                elif difficulty_choice == 4:
                    print("Sorry, currently doesn't works. Wait the next version.")
                else:
                    print("It's not a choice option")
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
