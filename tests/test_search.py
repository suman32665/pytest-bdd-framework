from pytest_bdd import scenario, given, when, then
from steps.searchBookSteps import *  # Import all step definitions


@scenario('../Features/SearchBook.feature', 'Search Books')
def test_search_book():
   pass
