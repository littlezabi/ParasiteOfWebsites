from email import message
import time
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from scrapper import Scrapper
from server_actions import Replyer
import variables as vars
import messages
from pass_check_bot import PasswordChecker as PC
from urllib import request, parse
from server_actions import Replyer


class Bot:
    """
        The main class of the bot is starting from here
    """

    def __init__(self):
        # self._options_ = Options()
        # self._options_.add_experimental_option(
        #     "debuggerAddress", f"127.0.0.1:9222")
        # self._options_.add_argument("user-data-dir=C:/whatsapp/")
        # self.driver = webdriver.Chrome(
        #     executable_path=vars.chromedriver, chrome_options=self._options_)
        self.replied = ''
        self.msg_box = ''

    def StoringCsv(self, text, file='files/logs.csv',  mode='a'):
        try:
            with open(file, mode, encoding='utf-8') as file:
                file.write(text)
        except Exception as e:
            print(e)
            print('CSV writing Error...')
        print('Stored in csv...')

    def SearchPassInCSV(self, text):
        try:
            with open('files/PassCheckerDataSet.csv', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.split(',')
                    if line[0].strip() == text.strip():
                        return line[1]
            return 'NotInCSV'
        except Exception as e:
            print('CSV file not found....')
            return 'CsvNotFound'

    def Reply(self, chat, chatType):
        if messages.wildcard in chat['text']:
            Replyer(messages.on_waiting, chat['id'])
            length = len(messages.wildcard)
            url = chat['text'][length:]
            scrap = Scrapper(url)
            Replyer(scrap.ouptup_message, chat['id'])
            return 1

        if "https://support.halabtech.com/" in chat['text'].lower():
            Replyer(messages.on_waiting, chat['id'])
            print('Matching...')
            if chatType == 'chat-unlock-url':
                search = self.SearchPassInCSV(chat['text'])
                if search == 'NotInCSV':
                    bot_ = PC(chat['text'])
                    bot_.RunAway()
                    bot_msg = bot_.secret_pass
                    if bot_msg == 'NotFound':
                        Replyer(messages.on_passcheck_notfound, chat['id'])
                    else:
                        Replyer(bot_msg, chat['id'])
                        text = chat['text'] + ',' + bot_msg + '\n'
                        self.StoringCsv(
                            text, 'files/PassCheckerDataSet.csv', 'a')
                elif search == 'CsvNotFound':
                    pass
                else:
                    Replyer(search, chat['id'])
                return 1
            elif "https://support.halabtech.com/index.php" in chat['text'].lower():
                Replyer(messages.on_waiting, chat['id'])
                scrap = Scrapper(chat['text'])
                Replyer(scrap.ouptup_message, chat['id'])
            elif "https://support.halabtech.com/" == chat['text'].lower() or "https://support.halabtech.com/index.php?a=account" == chat['text'].lower() or "https://support.halabtech.com" == chat['text'].lower():
                print('only browser open request => ON blues opening Scrapper...')
                Replyer(messages.on_waiting, chat['id'])
                scrap = Scrapper(chat['text'],
                                 open_only_browser=True)
                Replyer(scrap.ouptup_message, chat['id'])

        else:
            with open(vars.dictionary, 'r', encoding='utf-8') as dictionary:
                dictionary = dictionary.readlines()
                for text in dictionary:
                    if len(text) > 2:
                        msg = text.split(',')[0].lower()
                        reply = text.split(',')[1]
                        html_msg = chat['text'].lower()
                        if msg in html_msg:
                            if len(msg) > 0:
                                Replyer(reply, chat['id'])
                                break
                            else:
                                pass
                        else:
                            pass
                            # Replyer(
                            #     messages.on_not_any_reply_found, chat['id'])

    # def connection(self):
    #     try:
    #         self.msg_box = self.driver.find_element_by_css_selector(
    #             '#main > footer > div._2BU3P.tm2tP.copyable-area > div > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text')
    #         html_src = self.driver.page_source
    #         html = bs4(html_src, 'html.parser')
    #         html = html.select('._1Gy50')
    #         for i in range(1, 4):
    #             html_src = self.driver.page_source
    #             html = bs4(html_src, 'html.parser')
    #             html = html.select('._1Gy50')
    #             self.recentMsg1 = html[-1].getText()
    #             try:
    #                 if i == 1:
    #                     self.replied = html[-1].getText()
    #                     self.Reply(-1, html)
    #                 # if i == 2:
    #                 #     if html[-2].getText() != messages.on_waiting or self.replied != html[-2].getText():
    #                 #         self.replied = html[-2].getText()
    #                 #         self.Reply(-2, html)
    #             except:
    #                 pass

    #     except Exception as e:
    #         print(e)


# https://support.halabtech.com/index.php?a=downloads&b=file&id=536857
