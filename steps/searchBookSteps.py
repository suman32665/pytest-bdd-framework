from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from pages.searchPage import SearchPage
import pytest

@given("I open the book store page")
def open_SearchBook_page(browser):
    browser.get("https://demoqa.com/books")
    return SearchPage(browser)

@when("I search for book")
def search_book(browser):
    searchPage = SearchPage(browser)
    searchPage.enter_book("git")

@then("I should see the book in result")
def Verify_result_book(browser):
    searchPage = SearchPage(browser)
    searchPage.VerifyBookResult()