from time import sleep
import urllib.request
from bs4 import BeautifulSoup as bs
from datetime import datetime
from bot import Parasite
from request_ import ServerRequest
import messages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import variables as vars


class Scrapper:
    def __init__(self, url, open_only_browser=False, by_force=False) -> None:
        self.retries = 2
        self.ouptup_message = ''
        if open_only_browser == True:
            print('Paraiste Done his process now referring to the Parasite.CrackMindBot')
            parasite = Parasite(linktype='Featured')
            parasite.CrackedMindBot(url, open_only_browser=True)
            self.ouptup_message = parasite.end_url
            return 1
        else:
            self.findinfolders(url, by_force)

    def findinfolders(self, url, by_force):
        if by_force == False:
            checkExistince = self.CheckInDataSet(url.strip())
            if checkExistince == 1:
                print('Already Exist...')
                self.ouptup_message = messages.on_file_exist_in_server
                return 1
        content = self.Requester(url)
        html = bs(content, 'html.parser')
        title = html.title

        featured = 'Free'
        filesize = ''
        link_ = ''
        lable_info = ''
        description = ''
        try:
            try:
                title = html.select('.file-title.page-title')[0].getText()
            except:
                pass
            try:
                file_details = html.select('div.file-details')[0].select('div.col-md-12.col-sm-12.col-xs-12.no-margin.no-padding')[
                    0].select('table.table')[0].select('tbody')[0].select('tr')
            except:
                pass
            try:
                date = file_details[0].select('td')[1].getText()
            except:
                pass
            try:
                filesize = file_details[1].select('td')[1].getText()
            except:
                pass
            file_meta = html.select('div.file-meta')
            try:
                description = file_meta[0].select(
                    'p.file-description')[0].getText()
            except:
                pass
            lable_info = file_meta[0].select(
                'span.label.label-info')[0].getText()
        except:
            pass
        if lable_info == 'Featured':
            featured = 'Featured'
        else:
            if vars.ProcessOnNoneFeaturedFiles:
                self.ouptup_message = messages.on_file_not_featured
                return 1

        try:
            link_ = html.select('div.file-download')[0].select(
                'a.btn.btn-lg.btn-success.btn-block.btn-download')[0].get('href')
        except:
            print('Link not found')
        # clicking on download button

        if len(link_) < 1:
            print('link is invalid or not correct url check it manually')
            self.ouptup_message = messages.on_manual_check_request
            return 1

        parasite = Parasite(lable_info)
        parasite.CrackedMindBot(link_)
        drive_url = parasite.end_url

        if 'https://drive.google.com/' in drive_url or 'https://mega.nz/file' in drive_url or 'DirectDownload' in drive_url:
            if 'DirectDownload' in drive_url:
                self.ouptup_message = messages.on_direct_download
                return 1
            if len(filesize) > 0:
                try:
                    integers = filesize.split('.')
                    integers_in = integers[1]
                    integers = int(integers[0])
                    if 'KB' in integers_in or 'kb' in integers_in:
                        filesize = (integers * 1000)
                    if 'MB' in integers_in or 'mb' in integers_in:
                        filesize = (integers * 1000) * 1000
                    if 'GB' in integers_in or 'gb' in integers_in:
                        filesize = ((integers * 1000) * 1000) * 1000
                    if 'TB' in integers_in or 'tb' in integers_in:
                        filesize = ((integers * 1000) * 1000) * (1000 * 1000)
                except:
                    pass

            created_date = datetime.today().strftime('%Y-%m-%d')
            data = {
                'bot_request': 1,
                'url': drive_url,
                'title': title,
                'size': filesize,
                'date': created_date,
                'description': description
            }
            print('Refferring to server for storing...')

            if 'DirectDownload' in drive_url:
                # data['url'] = messages.def_download_url
                self.ouptup_message = messages.on_direct_download
                return 1
            if by_force == False:
                server_response = ServerRequest(data).send_request()
            else:
                server_response = ServerRequest(data, 'update').send_request()

            if server_response == 'Success' or server_response == 'updated':
                print('Saved...Successfuly')

                if 'DirectDownload' in drive_url:
                    self.ouptup_message = messages.on_direct_download
                    self.SavingInFile(url)
                    return 1
                else:
                    self.ouptup_message = messages.after_server_success
                try:
                    if by_force == False:
                        text = url.strip()
                        text = text + '\n'
                        self.SavingInFile(text)
                    return 1
                except Exception as e:
                    print(e)
                    return 1

            if server_response == 'AlreadyExist':
                print('Already Exist...')
                self.ouptup_message = messages.on_file_exist_in_server
                text = url.strip()
                text = text + '\n'
                self.SavingInFile(text)
                return 1

            if server_response == 'Error':
                self.ouptup_message = messages.after_server_error

        else:
            self.ouptup_message = messages.default_message

    def CheckInDataSet(self, url):
        print('Searching Existence of url...')
        try:
            with open('files/dataset.csv', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line == url:
                        return 1
            return 0
        except Exception as e:
            print(e)

    def SavingInFile(self, text):
        try:
            with open('files/dataset.csv', 'a', encoding='utf-8') as file:
                file.write(text)
            print('Saved in file')
        except Exception as e:
            print(e)

    def Requester(self, url):
        return self.ScrapWithSel(url)
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

    def ScrapWithSel(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option(
            'useAutomationExtension', False)
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("user-data-dir=C:/SCRAPhalabtech-cache")
        chrome_options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(
            options=chrome_options, executable_path="chromedriver.exe")
        driver.get(url)
        sleep(3)
        page_src = driver.page_source
        driver.close()
        return page_src


# Scrapper('https://support.halabtech.com/index.php?a=downloads&b=file&id=529592')
