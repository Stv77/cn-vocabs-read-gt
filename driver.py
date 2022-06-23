from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

#read bbc uk article for 1 minute
def search_on_bbc():
    driver.get('https://www.bbc.co.uk/search')
    input = driver.find_element_by_css_selector('input#search-input')
    input.click()
    input.send_keys(Keys.CONTROL, 'v')
    input.send_keys(Keys.ENTER)
    time.sleep(60)

#Read Chinese New York Times
def search_on_nyt():
    driver.get('https://cn.nytimes.com/')
    input = driver.find_element_by_css_selector('input.searchQuery')
    input.click()
    input.send_keys(Keys.CONTROL, 'v')
    input.send_keys(Keys.ENTER)
    time.sleep(60)