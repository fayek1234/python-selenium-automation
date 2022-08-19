# Create by khizir chuwdhury
Feature: Test scenarios for order

    Scenario: logged out user see sign in page
      Given open amazon page
      When  user click on order
      Then user see result
     # Then user can search for email