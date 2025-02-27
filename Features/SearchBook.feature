Feature: Search Functionality

  Scenario: Search Books
    Given I open the book store page
    When I search for book
    Then I should see the book in result
