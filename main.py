# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os

'''
    Update your chrome
    Download the latest chromedriver
    Put all the papers in one directory and update to "paper_dir"
    If your chrome says "THE SITE CAN'T BE REACHED", please feel free to close it and try again, again... 
'''

def openChrome():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # set your chromedriver path
    driver = webdriver.Chrome(executable_path='XXX\\chromedriver.exe', chrome_options=option)
    return driver

def login(driver):
    elem = driver.find_element_by_name("XXX") # Conference ID
    elem.send_keys("XXX")
    
    elem = driver.find_element_by_name("XXX")
    elem.click()

def submit_one(driver, paper_id):
    driver.find_element_by_xpath("//input [@type=\"submit\"]").click()

    print('{} submitted successfully'.format(paper_id))


# url = "XXX"
url = 'XXX'
paper_dir = 'XXX'

if __name__ == '__main__':
    paper_name_list = os.listdir(paper_dir)
    
    driver = openChrome()
    driver.get(url)

    login(driver)

    for name in paper_name_list:
        print('id:{}'.format(name[:-4]))
        submit_one(driver, name[:-4])