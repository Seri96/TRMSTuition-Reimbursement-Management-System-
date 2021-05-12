from selenium.webdriver.chrome.webdriver import WebDriver


class TrmsHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        return self.driver.find_element_by_id('username')

    def password(self):
        return self.driver.find_element_by_id('password')

    def login_button(self):
        return self.driver.find_element_by_id('loginButton')

    def date(self):
        return self.driver.find_element_by_id('date')

    def time(self):
        return self.driver.find_element_by_id('time')

    def location(self):
        return self.driver.find_element_by_id('location')

    def description(self):
        return self.driver.find_element_by_id('description')

    def cost(self):
        return self.driver.find_element_by_id('cost')

    def grade(self):
        return self.driver.find_element_by_id('gradingFormat')

    def event(self):
        return self.driver.find_element_by_id('typeOfEvent')

    def justification(self):
        return self.driver.find_element_by_id('justification')

    def form_submit(self):
        return self.driver.find_element_by_id('createFormButton')

    def message(self):
        return self.driver.find_element_by_id('message')
