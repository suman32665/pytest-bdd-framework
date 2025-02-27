from pytest_bdd import scenario, given, when, then
from steps.loginSteps import *  # Import all step definitions


@scenario('../Features/login.feature', 'Valid login')
def test_valid_login():
   pass
