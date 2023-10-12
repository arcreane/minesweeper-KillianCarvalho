
def get_user_action():
    coord_x = get_int_user("Choose a X → coordinate : ")
    coord_y = get_int_user("Choose a Y ↑ coordinate : ")
    action = get_int_user("Choose an action:\n\t1- returned\n\t2- flagged")
    if action == 1:
        action = 'R'
    elif action == 2:
        action = 'F'
    return coord_x, coord_y, action

def get_int_user(request):
    print(request)

    return_user = input("> ")

    try:
        val = int(return_user)
        return val
    except:
        print("please enter a valid choice")