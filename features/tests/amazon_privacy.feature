# Created by khizir at 8/5/2022
Feature: window handling test case

  Scenario: user can open and close Amazon privacy Notice
    Given Open Amazon T&C  page
    When Store original windows
    And click on Amazon Privacy Notice link
    And Switch to new opened window
    Then verify user can see Amazon privacy Notice  page is Opened
    And user can close new window
    And go back to original window
