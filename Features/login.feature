Feature: Login Functionality

  Scenario: Valid login
    Given I open the login page
    When I enter valid username and password
    And I click on the login button
    Then I should see the homepage