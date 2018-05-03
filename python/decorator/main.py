from user import User
from random import random

def login_required(f):
    def new_f(*args, **kwargs):
        a = args[0]
        print(a)
        print('checking login names')
        if not a:
            return 'not sign in!'
        elif a.name not in User.get_usernames():
            return 'not in database!'
        else:
            print('logged in')
            return f(*args, **kwargs)
    return new_f

def game_maker_auth_required(f):

    @login_required
    def wrapper(*args, **kwargs):
        print('checking game_maker status')
        a = args[0]
        if not a.is_maker:
            return 'does not have permission !'
        else:
            print('have permission...')
            return f(*args, **kwargs)
    return wrapper


@game_maker_auth_required
def change_name(curr_user, to_name):
    curr_user.name = to_name
    return 'changed name'

def main():
    num_loops = 5
    char_start = ord('a')
    start_range = 8

    chars = [chr(x) for x in range(char_start, char_start + num_loops)]
    nums = [x for x in range(start_range, start_range + num_loops)]
    for char, num in zip(chars, nums):
        u = User(name=char, val=num, is_maker=(random() <= 0.5))
        User.add_to_database(u)
        print(change_name(u, u.name + '_changed'))
        print(u)
        print()

    user = User(name='x', val='400000', is_maker=True)
    print(change_name(user, user.name + '_changed'))
    print()

    user = User(name='x', val='400000', is_maker=False)
    print(change_name(user, user.name + '_changed'))
    print()

    user = None
    print(change_name(user, 'blank_changed'))

if __name__ == '__main__':
    main()