import vk
import getpass

APP_ID = 5661627


def get_user_login():
    return input('Enter your login: ')


def get_user_password():
    return getpass.getpass('Enter your password: ')


def get_online_friend_names(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    online_friend_ids = api.friends.getOnline()
    return api.users.get(user_ids=online_friend_ids)


def output_friends_to_console(friends_online):
    number_of_friends_online = len(friends_online)
    if number_of_friends_online:
        print('There are %d friends online:' % number_of_friends_online)
        for friend in friends_online:
            print(friend['first_name'], friend['last_name'])
    else:
        print('There are no friends online :(')


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    online_friends = get_online_friend_names(login, password)
    output_friends_to_console(online_friends)
