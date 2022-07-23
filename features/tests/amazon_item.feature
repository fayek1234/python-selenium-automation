# Created by khizir at 7/23/2022
Feature: see one item on cart page


  Scenario: User can add a product to the cart
    Given open amazon page
    When search for pink vinyl disposable Gloves - 200 pack
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
