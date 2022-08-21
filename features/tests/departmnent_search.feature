# Created by khizi at 8/19/2022
Feature: test case for department search

  Scenario: user can select and search in a department
    Given Open Amazon page
    When select department computers
    And search for hp laptop
    Then verify computers department is selected
