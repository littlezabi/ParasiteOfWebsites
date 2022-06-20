# muhammadayyan942@gmail.com
# Pass.halabtech.com
# https://support.halabtech.com/index.php?a=downloads&b=file&id=528351

from bs4 import BeautifulSoup as bs
import urllib.request
from selenium import webdriver
from time import sleep


class PasswordChecker:
    def __init__(self, url) -> None:
        self.retries = 2
        self.url = url
        self.secret_pass = ''
        self.password_checker_url = 'https://pass.halabtech.com/'
        self.email = 'muhammadayyan942@gmail.com'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("user-data-dir=C:/halabtecpass-cache")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        self.bot = webdriver.Chrome(
            options=chrome_options, executable_path="chromedriver.exe")

    def RunAway(self):
        content = self.Requester(self.url)
        html = bs(content, 'html.parser')
        # print(html)
        filename = html.title.getText()
        filename = filename.split('|')[0].strip()
        self.RunOnFly(filename)

    def RunOnFly(self, filename):
        print('Password Bot Warm up...')
        self.bot.get(self.password_checker_url)
        sleep(3)
        retries = self.retries
        while retries != 0:
            print(retries)
            try:
                retries -= 1
                sleep(2)
                print('Entering data...')
                email = self.bot.find_element_by_css_selector(
                    'body > section > div > div > form > input[type=email]:nth-child(1)')
                file_selector = self.bot.find_element_by_css_selector(
                    'body > section > div > div > form > input[type=text]:nth-child(2)')
                email.clear()
                email.send_keys(self.email)
                file_selector.clear()
                file_selector.send_keys(filename)
                sleep(1)
                self.bot.execute_script(
                    "document.querySelector('body > section > div > div > form').submit()")
                retries = 0
                print('submitting form...')
                break
            except Exception as e:
                print(e)
                self.secret_pass = 'NotFound'

        sleep(3)
        try:
            print('finding elements...')
            mini_win = self.bot.find_element_by_css_selector(
                'body > div > div > div.swal-text')
            self.secret_pass = mini_win.text
            print('found: ', mini_win.text)
            self.bot.close()
            return
        except:
            sleep(3)
            try:
                print('finding elements...')
                mini_win = self.bot.find_element_by_css_selector(
                    'body > div > div > div.swal-text')
                print('found: ', mini_win.text)
                self.secret_pass = mini_win.text
                self.bot.close()
                return
            except:
                self.secret_pass = 'NotFound'
                self.bot.close()
        return

    def Requester(self, url):
        retries = self.retries
        while retries != 0:
            try:
                retries -= 1
                http = urllib.request.Request(url, headers={
                                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'})
                http = urllib.request.urlopen(http)
                if http.status == 200:
                    print('status: 200')
                    return http.read().decode('utf-8')

                else:
                    raise Exception
            except Exception as exception:
                print('status: ', exception)


# url = 'https://support.halabtech.com/index.php?a=downloads&b=file&id=528351'

# bot = PasswordChecker(url).RunAway()
