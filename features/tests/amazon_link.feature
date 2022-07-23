# Created by khizi at 7/23/2022
Feature: Test scenario to open best seller page then see some link


  Scenario:  click on amazon best seller page to see link
    Given open amazon page
    When click on best seller page
    Then verify 5 links
