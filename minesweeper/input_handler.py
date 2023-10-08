def get_user_action():
    return None


def get_int_user(request):
    print(request)

    return_user = input("> ")

    try:
        val = int(return_user)
        return val
    except:
        print("please enter a valid choice")
