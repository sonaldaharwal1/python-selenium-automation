
Feature: Target “Your cart is empty” message is shown tests

  Scenario: User can see “Your cart is empty” message is shown on target
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown