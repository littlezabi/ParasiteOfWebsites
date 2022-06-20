from urllib import request, parse
from variables import server_file


class ServerRequest:
    def __init__(self, data={}, action='insert') -> None:
        self.data = data
        self.data['action'] = action
        self.request_file = server_file

    def CheckInServer(self, title={}):
        print("Checking Existince...")
        title = parse.urlencode(title).encode()
        req = request.Request(self.request_file, data=title)
        responses = request.urlopen(req)
        responses = responses.read().decode('utf-8')
        return responses

    def send_request(self):
        print('Saving in database....')
        data = parse.urlencode(self.data).encode()
        req = request.Request(self.request_file, data=data, headers={
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'})
        response = request.urlopen(req)
        response = response.read().decode('utf-8')
        return response

# data = {'bot_request': 1, 'url': 'https://drive.google.com/file/d/1q8a3wmaB8J8S-MEjYKcm6Io1wJwo0UFy/view', 'title': 'A307FN U2 Android 11 ROOT (A307FNXXU2CUF3) File By (Support.HalabTech.Com).tar', 'size': 36000000, 'date': '2021-10-19', 'description': ''}
# data['action'] = 'update'
# # print(data)
# res = ServerRequest(data, 'insert').send_request()
# print(res)
