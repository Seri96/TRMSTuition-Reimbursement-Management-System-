from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.trms_home import TrmsHomePage

# All setup and teardown functions must go in this file.
# These functions must be named using behave's conventions


def before_all(context):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver: WebDriver = webdriver.Chrome(
        '/Users/chrissei/Desktop/chromedriver', chrome_options=options)

    trms_home_page = TrmsHomePage(driver)

    context.driver = driver
    context.trms_home_page = trms_home_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
