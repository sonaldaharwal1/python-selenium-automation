
Feature: Tests for target circle page

  Scenario: Verify page has correct amount links
    Given Open target Circle page
    Then  Verify page has 10 links
      Then Verify can click every link