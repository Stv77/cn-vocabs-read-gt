from mandarin_vocabs import mandarin_vocabs
from driver import driver
import time
from selenium.webdriver.common.keys import Keys

driver.get('https://translate.google.com/?sl=zh-CN&tl=en&op=translate')
driver.maximize_window()

#checking if number is within range
def InRange(number, first_num, last_num):
    return first_num <= number <= last_num

def pause(determiner):
    if InRange(number=determiner, first_num=1,last_num=3) == True:
        return 3
    elif InRange(number=determiner, first_num=1, last_num=18) == True:
        return 7
    elif InRange(number=determiner, first_num=1, last_num=33) == True:
        return 11
    elif InRange(number=determiner, first_num=1, last_num=45) == True:
        return 14
    elif InRange(number=determiner, first_num=1, last_num=70) == True:
        return 20
    elif determiner > 70:
        return 60

def clear(determiner):
    determiner.send_keys(Keys.CONTROL, 'a')
    determiner.send_keys(Keys.BACKSPACE)

def read_article():
    driver.get('https://cn.nytimes.com/')
    driver.refresh()
    input = driver.find_element_by_css_selector('input.searchQuery')
    input.click()
    input.send_keys(current_word)
    input.send_keys(Keys.ENTER)
    time.sleep(60)
    driver.get('https://translate.google.com/?sl=zh-CN&tl=en&op=translate')

for x in range(len(mandarin_vocabs)):
    words_len = len(mandarin_vocabs[x])
    current_word = mandarin_vocabs[x]

    fill = driver.find_element_by_css_selector('div.QFw9Te > textarea')
    fill.click()
    fill.send_keys(mandarin_vocabs[x])
    fill.send_keys(Keys.ENTER)
    time.sleep(3)
    read_cn = driver.find_element_by_css_selector('button.VfPpkd-Bz112c-LgbsSe.VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe.fzRBVc.tmJved.DiOXab.SSgGrd.m0Qfkd')
    read_en = driver.find_element_by_css_selector('button.VfPpkd-Bz112c-LgbsSe.VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe.fzRBVc.tmJved.DiOXab.SSgGrd.Tw0Tv.m0Qfkd')
    
    #Read
    for x in range(2):
        read_cn.click()
        time.sleep(pause(words_len))
        read_en.click()
        time.sleep(pause(words_len))
    clear(determiner=fill)
    time.sleep(3)