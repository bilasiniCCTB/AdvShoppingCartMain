import sys
import datetime
from selenium import webdriver
import adshopcart_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
s = Service(executable_path='../chromedriver')


driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setUp():
    print(f'Test starts at: {datetime.datetime.now()}')
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Advantage Shopping  application website
    driver.get(locators.adshopcart_URL)

    # Checking that we're on the correct URL address and we're seeing correct title
    print('Hi'+driver.title+'Hello')
    print(driver.current_url)

    if driver.current_url == locators.adshopcart_URL and driver.title == ' Advantage Shopping':
        print(f'We\'re at advantage online shopping HOMEPAGE -- {driver.current_url}')
        print(f'We\'re  title message --{driver.title} ')
    else:
        print(f'We\'re not at the advantage online shopping homepage. Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


