
Feature: Target products search tests

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for rice cooker
    Then Verify search results shown for rice cooke


  Scenario: User can search for an toaster
    Given Open target main page
    When Search for toaster
    Then Verify search results shown for toaster

  Scenario: User can search for a headphone
    Given Open target main page
    When Search for headphone
    Then Verify search results shown for headphone
