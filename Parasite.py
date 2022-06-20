import time
from blues import Bot
# from variables import reply_speed, chat_by_target_user
from server_actions import get_from_server
# from bot import Parasite

# halab_bot = Parasite()
# halab_bot.bot_state = 1
bot = Bot()
chatType = ""
while True:
    try:

        if chatType == 'chat-unlock-url' or chatType == '':
            chatType = 'chat-password-url'
        elif chatType == 'chat-password-url':
            chatType = 'chat-unlock-url'

        data_list = get_from_server(chatType)
        for data in data_list:
            print('user: ', data['username'],
                  ' | msg: ', data['text'] + ' ' * 30, end='\r')
            bot.Reply(data, chatType)
    except Exception as e:
        print(e)

    time.sleep(2)
