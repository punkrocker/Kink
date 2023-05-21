from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import TimeoutException
import time
from dto.Shoot import Shoot

browser = webdriver.Edge(executable_path='./msedgedriver.exe')
# browser = webdriver.Chrome(service=Service('./chromedriver.exe'))
# browser.implicitly_wait(15)
# browser.set_page_load_timeout(15)
browser.maximize_window()
browser.get('https://www.kink.com/login')
enter_kink = browser.find_element(By.XPATH, '//button[text()="Enter Kink"]')
enter_kink.click()

f = open('../login.info').readlines()
account = f[0]
pwd = f[1]

# login_button = browser.find_element(By.CSS_SELECTOR, '[class="nav-item d-none d-md-block"]')
# login_button.click()

username = browser.find_element(By.ID, 'usernameLogin')
username.click()
username.send_keys(account)
password = browser.find_element(By.ID, 'passwordLogin')
username.click()
password.send_keys(pwd)
# login_btn = browser.find_element('name', 'login')
login_btn = browser.find_element(By.ID, 'loginSubmit')
login_btn.click()
time.sleep(5)

def load_url(page_source):
    s = Shoot(page_source)
    for link in s.download_link:
        print(link)

browser.get("https://www.kink.com/shoot/104785")
# 不sleep会导致没有加载完下载链接
time.sleep(20)
load_url(browser.page_source)
browser.quit()
