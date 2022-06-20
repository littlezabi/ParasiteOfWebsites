
import base64
import json
from urllib import request, parse
from variables import live_chat_files_


def Replyer(text, chatID):
    text = text.encode('utf-8')
    text = base64.b64encode(text)
    data = {'botResponse': 1, 'text': text, 'chatID': chatID}
    data = parse.urlencode(data).encode()
    req = request.Request(live_chat_files_, data=data, headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'})
    response = request.urlopen(req)
    response = response.read().decode('utf-8')
    print('Replied: '+response)


def get_from_server(chatType):
    data = {'getChats': 1, 'chatType': chatType}
    data = parse.urlencode(data).encode()
    req = request.Request(live_chat_files_, data=data, headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'})
    response = request.urlopen(req)
    response = response.read().decode('utf-8')
    response = json.loads(response)
    return response
