
Feature: Target products search tests

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for rice cooker
    Then Verify search results shown for rice cooker
    Then Verify correct search results url opens for rice cooker

  Scenario: User can search for an mug
    Given Open target main page
    When Search for mug
    Then Verify search results shown for mug
    Then Verify correct search results url opens for mug

  Scenario: User can search for a headphone
    Given Open target main page
    When Search for headphone
    Then Verify search results shown for headphone
