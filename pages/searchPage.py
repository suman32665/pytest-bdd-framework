from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.XPATH, "//*[@id='searchBox']")
        self.result_book = (By.XPATH, "//*[text()='Git Pocket Guide']//parent::*/parent::*/parent::*/following-sibling::*[text()='Richard E. Silverman']")

    def enter_book(self, book):
        self.driver.find_element(*self.search_input).send_keys(book)

    def VerifyBookResult(self):
        self.driver.find_element(*self.result_book)