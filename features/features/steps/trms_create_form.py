from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.trms_home import TrmsHomePage


@given('The User is on the Create Form Page')
def get_to_create_page(context):
    driver: WebDriver = context.driver
    driver.get('http://0.0.0.0:8080/createform.html')


@when('The User types {date} in the date input')
def type_into_date(context, date):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.date().send_keys(date)


@when('The User types {time} in the time input')
def type_into_time(context, time):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.time().send_keys(time)


@when('The User types {location} in the location input')
def type_into_location(context, location):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.location().send_keys(location)


@when('The User types {course_description} in the course description input')
def type_into_desc(context, course_description):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.description().send_keys(course_description)


@when('The User types {cost} in the cost input')
def type_into_cost(context, cost):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.cost().send_keys(cost)


@when('The User types {grade} in the grade input')
def type_into_grade(context, grade):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.grade().send_keys(grade)


@when('The User types {event} in the event input')
def type_into_event(context, event):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.event().selectByVisibleText(event)


@when('The User types {justification} in the grade input')
def type_into_justification(context, justification):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.justification().send_keys(justification)


@when('The User Clicks the Submit Button')
def click_submit(context):
    trms_home: TrmsHomePage = context.trms_home_page
    trms_home.form_submit().click()


@then('Form should be added successfully')
def form_added(context):
    driver: WebDriver = context.driver
    assert driver.message == "Form Successfully Added"
