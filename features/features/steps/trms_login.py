from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.trms_home import TrmsHomePage


@given('The User is on the Login Page')
def get_to_login_page(context):
    driver: WebDriver = context.driver
    driver.get('http://0.0.0.0:8080/login.html')


@when('The User types EmployeeBob in the username field')
def type_EmployeeUsername(context):
    trms_home_page: TrmsHomePage = context.trms_home_page
    trms_home_page.username().send_keys("EmployeeBob")


@when('The User types EmployeeBob in the username field')
def type_EmployeePassword(context):
    trms_home_page: TrmsHomePage = context.trms_home_page
    trms_home_page.password().send_keys("passwerd")


@when('The User clicks on the login button')
def type_employee_log(context):
    trms_home_page: TrmsHomePage = context.trms_home_page
    trms_home_page.login_button().click()


@then('The User should be on the Form Page')
def on_form(context):
    driver: WebDriver = context.driver
    assert driver.title == "Form"


@when('The User types BencoBob in the username field')
def type_benco_username(context):
    trms_home_page: TrmsHomePage = context.trms_home_page
    trms_home_page.username().send_keys("BencoBob")


@when('The User types BencoBob in the passwerd field')
def type_benco_password(context):
    trms_home_page: TrmsHomePage = context.trms_home_page
    trms_home_page.password().send_keys("passwerd")


@when('The User clicks on the login button')
def type_benco_log(context):
    trms_home_page: TrmsHomePage = context.trms_home_page
    trms_home_page.login_button().click()


@then('The User should be on the Benco Page')
def on_benco_form(context):
    driver: WebDriver = context.driver
    assert driver.title == "Benco"
