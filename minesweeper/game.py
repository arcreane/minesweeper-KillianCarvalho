import sys
import config
import board
import input_handler
import display

def start_game():
    # say hello
    display.print_welcome()
    display.start_menu()
    user_action = input_handler.get_user_action()
    if user_action == 1:
        # init game
        pass
    elif user_action == 2:
        # charge game
        pass
    else:
        sys.exit()
    display.print_difficulty()
    user_diff = input_handler.get_user_difficulty()

if __name__ == "__main__":
    start_game()
