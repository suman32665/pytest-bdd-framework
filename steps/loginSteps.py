from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from pages.loginPage import LoginPage
import pytest

@given("I open the login page")
def open_login_page(browser):
    browser.get("https://demoqa.com/login")
    return LoginPage(browser)

@when("I enter valid username and password")
def enter_credentials(browser):
    login_page = LoginPage(browser)
    login_page.enter_username("suman1")
    login_page.enter_password("Newpass5!")

@when("I click on the login button")
def click_login(browser):
    login_page = LoginPage(browser)
    login_page.click_login()

@then("I should see the homepage")
def verify_homepage(browser):
    login_page = LoginPage(browser)
    assert ("suman1" == login_page.GetUserName())
