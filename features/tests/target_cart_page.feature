Feature: Target’s product into the cart shown tests

  Scenario: User can see “product into the cart” on target
    Given Open target main page
    When Search for coffee
    When Add coffee into cart
    When Chose option and add coffee into cart
    When Click on view cart & check out
    Then Verify cart result shown for item




