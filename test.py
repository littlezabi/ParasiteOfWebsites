from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
options = Options()
options.add_argument('--proxy-server=1.1.1.1:432')
options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get("https://telegram.org")

# driver.quit()