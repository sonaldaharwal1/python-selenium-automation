#
Feature: Test cases for open and close Terms and Conditions

  Scenario: Scenario: User can  from sign in page
 Given  Open target main page
   When   Click Sign In
   When   From right side menu & click Sign In
 #Given Open sign in page
  Given Store original window
  When Click on Target terms and conditions link
  And Switch to the newly opened window
  Then Verify Terms and Conditions page is opened
  And Close current page
  And Return to original window