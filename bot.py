from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import messages

super_links = []
login_auth = []
user_details = open('files/users.csv', 'r').readlines()
avoid_first_line = 0
for user in user_details:
    if avoid_first_line:
        array = []
        user = user.split(',')
        array.append(user[0].strip())
        array.append(user[1].strip())
        login_auth.append(array)
    avoid_first_line = 1
self_fixing = 1
page_load_time = 1
content_load_time = 2
retries = 2
login_trys = 0
def_login_page_url = 'https://support.halabtech.com/index.php?a=login'
def_email = 'waqassial861@gmail.com'
def_password = 'waqassial9'


class Parasite:
    global content_load_time
    global page_load_time

    def __init__(self, linktype=''):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--log-level=3")
        if linktype == 'Featured':
            chrome_options.add_argument(
                "user-data-dir=C:/halabtech-featured-cache")
        else:
            chrome_options.add_argument("user-data-dir=C:/halabtech-cache")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        self.bot = webdriver.Chrome(
            options=chrome_options, executable_path="chromedriver.exe")
        self.retries = retries
        self.login_input = 0
        self.login_trys = 1
        self.end_url = ''
        self.url = ''

    def OpenOnlyInBrowser(self, url):
        self.bot.get(url)

    def CrackedMindBot(self, url, open_only_browser=False):
        if open_only_browser == True:
            self.OpenOnlyInBrowser(url)
            self.end_url = messages.on_browser_open_request
            return 1
        self.url = url
        print('opening: '+url)
        global retries
        self.retries = 0
        while self.retries != retries:
            self.retries = self.retries + 1
            try:
                self.bot.get(url)
                time.sleep(page_load_time)
                crnt_url = self.bot.current_url
                if def_login_page_url in crnt_url:
                    print('login url found redirecting to login page...')
                    self.login()
                break
            except Exception as e:
                print(str(e))
                time.sleep(2)

        if self.retries == retries:
            self.end_url = messages.damage_error
        else:
            self.WalkOn()

    def WalkOn(self):
        print('Fetcing Actual url..........')
        # time.sleep(page_load_time)
        self.retries = 0
        try:
            page_source = self.bot.page_source
            html = BeautifulSoup(page_source, 'html.parser')
            anchor = ''
            try:
                html.select(
                    '.inline-width.pad-b-40.width-100per.single-download-content')
                html.select('.file-download')
                anchor = html.select(
                    '.btn.btn-lg.btn-success.btn-block.btn-download')
                anchor = anchor[0].get('href')
            except:
                pass

            if 'utoken' in anchor:
                try:
                    self.bot.get(anchor)
                    time.sleep(1)
                    anchor = self.bot.current_url
                    if 'https://drive.google.com/' in anchor or 'https://mega.nz/file' in anchor:
                        self.end_url = anchor
                        self.bot.close()
                        return
                    else:
                        self.end_url = 'DirectDownload'
                        self.bot.close()
                        return
                except:
                    self.end_url = 'ErrorOccured'
                return

        except Exception as e:
            if 'list index out of range' in e:
                print('\a\a')
                self.end_url = messages.damage_error
                return

        time.sleep(2)

        if self.retries == retries:
            try:
                elem = self.bot.find_element_by_css_selector(
                    '#pop-alert-modal > div > div > div.modal-header.\?\$color.bg-red.\$color > h4')
                if elem.text == 'Package not able to download':
                    print('stopping at: ', self.bot.current_url)
                    print('\a Login Again please...')
                    self.logout()
                    self.login()
            except:
                pass
            try:
                elem = self.bot.find_element_by_css_selector(
                    '#pop-alert-modal > div > div > div.modal-header.\?\$color.bg-blue.\$color > h4')
                if elem.text == 'Fair usage bandwidth exceeded':
                    self.logout()
                    self.login()
            except:
                pass
            try:
                time.sleep(content_load_time)
                btn = self.bot.find_element_by_css_selector(
                    '#device-grant-modal > div > div > form > div.modal-footer > button.btn.btn-success.btn-lg.pull-left')
                btn.send_keys(Keys.RETURN)
                time.sleep(2)
                self.WalkOn(self.bot.current_url)
            except:
                print('\a\a')
                self.end_url = messages.contact_with_adming

        else:
            print('\a\a')
            self.end_url = messages.contact_with_adming

    def login(self):
        self.login_trys = self.login_trys - 1
        if 'https://support.halabtech.com/index.php?a=login' not in self.bot.current_url:
            self.bot.get('https://support.halabtech.com/index.php?a=login')
            time.sleep(page_load_time)
        try:
            try:
                self.bot.execute_script(
                    "const element = document.querySelector('#pop-alert-modal');element.click();")
            except:
                pass
            time.sleep(content_load_time)
            email = self.bot.find_element_by_css_selector(
                'body > div.wrapper > div > div:nth-child(1) > div > form > div:nth-child(3) > input')
            email.clear()
            print('Email: '+login_auth[self.login_input][0])
            _email = login_auth[self.login_input][0]
            email.send_keys(_email)
            password = self.bot.find_element_by_css_selector(
                'body > div.wrapper > div > div:nth-child(1) > div > form > div:nth-child(4) > input')
            password.clear()
            _password = login_auth[self.login_input][1]
            print('Password: '+login_auth[self.login_input][1])
            self.login_input = self.login_input + 1
            password.send_keys(_password)
            checkbox = self.bot.find_element_by_css_selector(
                'body > div.wrapper > div > div:nth-child(1) > div > form > div:nth-child(6) > span.pull-left > label > input')
            checkbox.send_keys(Keys.SPACE)
        except Exception as e:
            print(e)
        captcha = 1
        if captcha:
            self.setCaptcha()

    def logout(self):
        try:
            print('Logout.....')
            self.bot.get('https://support.halabtech.com/index.php?a=logout')
            time.sleep(page_load_time)
            btn = self.bot.find_element_by_css_selector(
                'body > nav > div > div.col-md-8.col-sm-8.col-xs-12.no-margin > ul > li:nth-child(2) > a')
            btn.send_keys(Keys.RETURN)
            time.sleep(1)
            print('Logout Successfully...')
        except Exception as e:
            print(e)

    def setCaptcha(self):
        print('\a\aBrowser is stopped in Login point please login....')
        self.end_url = messages.contact_with_adming
