import sys
import config
import board
import input_handler
import display

def start_game():
    # say hello
    display.print_welcome()

    start = False
    while not start:
        user_action = input_handler.get_int_user(display.start_menu())
        if user_action == 1:
            start = True
            valid_diff = False
            while not valid_diff:
                difficulty_choice = input_handler.get_int_user(display.print_difficulty())
                if difficulty_choice == 1:
                    grid_size = config.EASY_GRID_SIZE
                    nbr_mines = config.EASY_NUM_MINES
                    valid_diff = True
                elif difficulty_choice == 2:
                    grid_size = config.MEDIUM_GRID_SIZE
                    nbr_mines = config.MEDIUM_NUM_MINES
                    valid_diff = True
                elif difficulty_choice == 3:
                    grid_size = config.HARD_GRID_SIZE
                    nbr_mines = config.HARD_NUM_MINES
                    valid_diff = True
                elif difficulty_choice == 4:
                    print("Sorry, currently doesn't works. Wait the next version.")
                else:
                    print("It's not a choice option")
        elif user_action == 2:
            # charge game
            print("Sorry, the load functionality is for another version.")
        elif user_action == 3:
            sys.exit()
        else:
            print("It's not a choice option")


if __name__ == "__main__":
    start_game()
